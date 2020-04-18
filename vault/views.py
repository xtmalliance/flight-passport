# Create your views here.

from django.http import HttpResponse
from oauth2_provider.decorators import protected_resource
import json
from oauth2_provider.models import AccessToken
import re
from django.contrib.auth import get_user_model
import jwt
from oauth2_provider_jwt.utils import decode_jwt_user_info

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