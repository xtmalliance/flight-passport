
from oauth2_provider.settings import oauth2_settings
from django.conf import settings
from jwcrypto import jwk, jws
from jwcrypto.common import json_encode
import json
def sign_json(payload):
    '''
    For a payload sign using the OIDC private key and return signed JWS
    '''

    algorithms = getattr(settings, 'JWT_JWS_ALGORITHMS', 'RS256')
    if oauth2_settings.OIDC_RSA_PRIVATE_KEY:
        key = jwk.JWK.from_pem(oauth2_settings.OIDC_RSA_PRIVATE_KEY.encode("utf8"))
    jws_token = jws.JWS(payload = payload)
    
    jws_token.add_signature(key = key, alg=algorithms, protected= json_encode({"alg":"RS256","kid": key.thumbprint()}))
    
    sig = jws_token.serialize()
    s= json.loads(sig)
    
    return {"signed_json": s["protected"]+'.'+s["payload"]+'.'+s["signature"]}

