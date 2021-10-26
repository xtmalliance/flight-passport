

from django.views.generic import TemplateView
class HomePage(TemplateView):
	template_name = 'passport_homepage.html'


class NotFoundView(TemplateView):
    template_name = "404.html"
    
    
class ErrorView(TemplateView):
    template_name = "500.html"

    @classmethod
    def get_rendered_view(cls):
        as_view_fn = cls.as_view()

        def view_fn(request):
            response = as_view_fn(request)
			
            response.render()
            return response

        return view_fn
    


	
# def get_user(request):

# 	app_tk = request.META["HTTP_AUTHORIZATION"]
# 	m = re.search('(Bearer)(\s)(.*)', app_tk)

# 	app_tk = m.group(3)
	
# 	try:
# 		payload = decode_jwt_user_info(app_tk)
# 	except jwt.ExpiredSignatureError:
# 		msg = 'Signature has expired.'
# 		raise exceptions.AuthenticationFailed(msg)
# 	except jwt.DecodeError:
# 		msg = 'Error decoding signature.'
# 		raise exceptions.AuthenticationFailed(msg)
# 	except jwt.InvalidTokenError as je:
		
# 		raise exceptions.AuthenticationFailed()
# 	email = payload['sub']

# 	u = get_user_model()
# 	user = u.objects.get(email = email)
	

# 	return HttpResponse(
# 		json.dumps({
# 		    'username': user.username, 
# 		    'email': user.email}),
# 		content_type='application/json')
 
 
# class GetJWKS(View):

#     def get(self, request, *args, **kwargs):
#         jwks = {"keys":[json.loads(os.environ.get('JWKS_KEY'))]}
#         return JsonResponse(jwks)

