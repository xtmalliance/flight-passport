import ast
import json
import logging

try:
    from urllib.parse import urlencode, urlparse, parse_qs
except ImportError:
    from urllib import urlencode # noqa
    from urlparse import urlparse, parse_qs

from oauth2_provider.settings import oauth2_settings
from django.conf import settings
from django.utils.module_loading import import_string
from oauth2_provider import views
from oauth2_provider.http import OAuth2ResponseRedirect
from oauth2_provider.models import get_access_token_model

from .utils import generate_payload, encode_jwt




# Create your views here.


logger = logging.getLogger(__name__)


class MissingIdAttribute(Exception):
    pass


class IncorrectAudience(Exception):
    pass


class JWTAuthorizationView(views.AuthorizationView):

    def get(self, request, *args, **kwargs):        
        response = super(JWTAuthorizationView, self).get(request, *args,
                                                         **kwargs)   

        if request.GET.get('response_type', None) == 'token' \
                and response.status_code == 302:
            url = urlparse(response.url)
            params = parse_qs(url.fragment)
            
            if params:
                content = {
                    'access_token': params['access_token'][0],
                    'expires_in': int(params['expires_in'][0]),
                    'scope': params['scope'][0]
                }
                jwt = TokenView()._get_access_token_jwt(request, content)
                
                response = OAuth2ResponseRedirect(
                    '{}&access_token_jwt={}'.format(response.url, jwt),
                    response.allowed_schemes)
        return response


class TokenView(views.TokenView):
    def _get_access_token_jwt(self, request, content):
        extra_data = {}
        
        issuer = settings.JWT_ISSUER_DOMAIN
        payload_enricher = getattr(settings, 'JWT_PAYLOAD_ENRICHER', None)
        request_params = list(request.POST.keys())     
        
        token = get_access_token_model().objects.get(token=content['access_token'])            
        if payload_enricher:
            fn = import_string(payload_enricher)
            extra_data = fn(request)
            
        if 'scope' in content:
            extra_data['scope'] = content['scope']
            extra_data['typ'] = "Bearer"
            
            
        if 'audience' in request_params: 
            requested_audience = request.POST['audience']   
            audience_query = token.application.audience.all().only('identifier')
            all_audience = [audience.identifier for audience in audience_query]
            
            try: 
                assert requested_audience in all_audience
            except AssertionError as ae:
                raise IncorrectAudience()
            else:                
                extra_data['aud'] = requested_audience
                

        id_attribute = getattr(settings, 'JWT_ID_ATTRIBUTE', None)
        
        if id_attribute:            
            token_user = token.user            
            try: 
                assert token_user is not None
                id_value = getattr(token_user, id_attribute, None)
                if not id_value:
                    raise MissingIdAttribute()
            except AssertionError as ae: 
                id_value = token.application.client_id + "@clients"
            
            extra_data['sub'] = str(id_value)
        
        payload = generate_payload(issuer, content['expires_in'], **extra_data)
            
        if oauth2_settings.OIDC_RSA_PRIVATE_KEY:
            key = jwk.JWK.from_pem(oauth2_settings.OIDC_RSA_PRIVATE_KEY.encode("utf8"))
            kid = key.thumbprint()
        else: 
            kid =  settings.JWKS_KEY_ID
        
        headers = {'kid': kid}
        
        token = encode_jwt(payload, headers= headers)
        
        return token

    @staticmethod
    def _is_jwt_config_set():
        issuer = getattr(settings, 'JWT_ISSUER', '')
        private_key_name = 'JWT_PRIVATE_KEY_{}'.format(issuer.upper())
        private_key = getattr(settings, private_key_name, None)
        id_attribute = getattr(settings, 'JWT_ID_ATTRIBUTE', None)
        if issuer and private_key and id_attribute:
            return True
        else:
            return False

    def post(self, request, *args, **kwargs):
        
        response = super(TokenView, self).post(request, *args, **kwargs)
        
        content = ast.literal_eval(response.content.decode("utf-8"))
        request_grant_type = request.POST.get('grant_type')
        # Per the ASTM standards on UTM only the 'client_credentails' grant must be a JWT
        if response.status_code == 200 and 'access_token' in content:
            if not TokenView._is_jwt_config_set():
                logger.warning('Missing JWT configuration, skipping token build')
            else:
                
                try:
                    
                    token_raw = self._get_access_token_jwt(
                        request, content)
                    if not isinstance(token_raw, str):
                        token_raw = token_raw.decode('utf-8')
                    content['access_token'] = token_raw
                   
                except MissingIdAttribute:
                    response.status_code = 400
                    response.content = json.dumps({
                        "error": "invalid_request",
                        "error_description": "App not configured correctly. "
                                             "Please set JWT_ID_ATTRIBUTE.",
                    })
                    
                except IncorrectAudience:
                    response.status_code = 400
                    response.content = json.dumps({
                        "error": "invalid_request",
                        "error_description": "Incorrect Audience. "
                                             "Please set the appropriate audience in the request.",
                    })
                else:
                    content = json.dumps(content)
                    response.content = content
                    
        return response
