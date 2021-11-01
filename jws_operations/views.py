
import logging
from authprofiles.models import PassportApplication
from django.views.generic import View
from .utils import sign_json
# Create your views here.
import json
from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
logger = logging.getLogger(__name__)

@method_decorator(csrf_exempt, name="dispatch")
class SignView(View):
    def post(self, request, *args, **kwargs):
        request_body = json.loads(request.body.decode('utf-8'))
        try:
            client_id = request_body.get("client_id")
        except KeyError as ke:
            response = JsonResponse({'message': 'C'}) 
        try:
            client_secret = request_body.get("client_secret")
        except KeyError as ke:
            response = JsonResponse({'message': 'C'}) 
        try:
            data_to_sign =  request_body.get("raw_data")
        except KeyError as ke:
            response = JsonResponse({'error': 'client_id, client_secret and raw_data need to be provided'}) 
            logging.error("Invalid data provided in the post request %s" % ke)
        try: 
            print(client_id, client_secret)
            application = PassportApplication.objects.filter(client_id= client_id, client_secret = client_secret, client_class = 9).exists()
            assert application is not None
        except AssertionError as ae:
            response = JsonResponse({'error': 'client_id, client_secret and application type needs to be correctly configured on the server'}) 
        try:
            json_to_sign = json.dumps(data_to_sign)
        except Exception as e: 
            response = JsonResponse({'error': 'Invalid JSON provided to sign'}) 
        signed = sign_json(json_to_sign)
        
        response = JsonResponse(json.loads(signed))
        
        return response
        
        