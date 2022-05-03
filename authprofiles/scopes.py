# from .settings import oauth2_settings
from django.conf import settings

class BaseScopes(object):
    
    def get_all_scopes(self):
        """
        Return a dict-like object with all the scopes available in the
        system. The key should be the scope name and the value should be
        the description.

        ex: {"read": "A read scope", "write": "A write scope"}
        """
        raise NotImplementedError("")

    def get_available_scopes(self, application=None, request=None, *args, **kwargs):
        """
        Return a list of scopes available for the current application/request.

        TODO: add info on where and why this method is called.

        ex: ["read", "write"]
        """
        raise NotImplementedError("")

    def get_default_scopes(self, application=None, request=None, *args, **kwargs):
        """
        Return a list of the default scopes for the current application/request.
        This MUST be a subset of the scopes returned by `get_available_scopes`.

        TODO: add info on where and why this method is called.

        ex: ["read"]
        """
        raise NotImplementedError("")


class PassportScopes(BaseScopes):
    
    def get_all_scopes(self):
        """
        Return a dict-like object with all the scopes available in the
        system. The key should be the scope name and the value should be
        the description.

        ex: {"read": "A read scope", "write": "A write scope"}
        """
        return {"openid": "A read scope", "profile": "A write scope"}

    def get_available_scopes(self, application=None, request=None, *args, **kwargs):
        available_scopes = []
        if application:
            all_audiences = application.audience.all()
            for api in all_audiences: 
                all_api_scopes = api.scopes.all()
                for cur_scope in all_api_scopes:
                    available_scopes.append(cur_scope.name)

            # based on client class filter read / write scopes 
            
        return available_scopes

    def get_default_scopes(self, application=None, request=None, *args, **kwargs):
        """
        Return a list of the default scopes for the current application/request.
        This MUST be a subset of the scopes returned by `get_available_scopes`.

        TODO: add info on where and why this method is called.

        ex: ["read"]
        """
        return ['openid','profile']
