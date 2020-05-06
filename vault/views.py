# Create your views here.
from django.http import HttpResponse, JsonResponse
from oauth2_provider.decorators import protected_resource
import json
from oauth2_provider.models import AccessToken
import re
from django.contrib.auth import get_user_model
import jwt
from oauth2_provider_jwt.utils import decode_jwt_user_info
from django.views import View

def get_user(request):

	app_tk = request.META["HTTP_AUTHORIZATION"]
	m = re.search('(Bearer)(\s)(.*)', app_tk)

	app_tk = m.group(3)

	try:
	    payload = decode_jwt_user_info(app_tk)
	except jwt.ExpiredSignatureError:
	    msg = 'Signature has expired.'
	    raise exceptions.AuthenticationFailed(msg)
	except jwt.DecodeError:
	    msg = 'Error decoding signature.'
	    raise exceptions.AuthenticationFailed(msg)
	except jwt.InvalidTokenError:
	    raise exceptions.AuthenticationFailed()
	email = payload['sub']

	u = get_user_model()
	user = u.objects.get(email = email)


	return HttpResponse(
		json.dumps({
		    'username': user.username, 
		    'email': user.email}),
		content_type='application/json')
 
 
class GetJWKS(View):

    def get(self, request, *args, **kwargs):
        jwks = {"kty":"RSA","e":"AQAB","kid":"9343256b-5ea5-4f48-872e-14a297cfe93c","n":"yDUwIDNl5XR4HR8OlM-fVDsPdt0F8jjwr59E8rgo8TEHKoEWjazcVTdAxUjwsK1WihskvHkLjxd205O2A4j0_Fdu_6t86RB0SlnDTPpciCwmh9t6XKgKOc5i1SGU3SKwRRH2x8jwoJ7Pv0ROXvt5v2FnSkhgKPH1_SAuYIa8l-7dnnsq-c-z0cBdikVC5BJXVZtOWwa3pUgOy3554vvT5ZwkuNBJp1tprSZJPeimA8FdT2Ddf2OMlpAYvgqSlUoTc2RhJmqjupQ3Ku8qtzO_QYRaN6K_05GioyMMuyrskwSuc-TKeINgH-CnRNI6dM7nYV6cdmLCaDrSMb6HzNpumtPYmISOrOMp-IqFZJsWpaWeyq9S6_g5LrNTjnmFyJT2UWaCO75x1PHsitVxFwVf3SwuuazpaZ7Egpl6GzpvEirbBBMk_aCr_FRWZA1ypLJmf0-iF5zFFy0uBpEb0WbM5cZjZ7zQJP570tZF41wdTIhpGuV0EXtZmi-Md0Va2NLHmejy-Ne0YxIiThNzTiFvzRygKTTS3SP68mb2iX3PFAf73vzB1TS5LRjo0NGowvCVWqkwn56gGGOgMvLo1M7ND4X4KXUmm6xoc0uWg4xqhsLFbOb0zVHKw8CLZKbbV5yYWmEoUNe536QM4I6U26VsWSU_bBH7Vfxb7YRmMf9eMGs"}
        return JsonResponse(jwks)
