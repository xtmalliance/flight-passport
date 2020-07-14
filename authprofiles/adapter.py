
from allauth.account.adapter import DefaultAccountAdapter
from . import constants
import tldextract
from dotenv import load_dotenv, find_dotenv
from os import environ as env
from django.forms import ValidationError

ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)


class PassportAccountAdapter(DefaultAccountAdapter):

    def clean_email(self,email):        
        DOMAIN_WHITELIST = env.get(constants.DOMAIN_WHITELIST)
        domain = email.split("@")[1]
        white_listed_domain = [i for i in DOMAIN_WHITELIST.split(";")] 
        
        if domain in white_listed_domain:              
            ext = tldextract.extract(domain)            
            tld = ext.domain.upper()
            suffix = ext.suffix.upper()
            return email 
        else: 
            raise ValidationError('You are restricted from registering. Please contact admin.')
