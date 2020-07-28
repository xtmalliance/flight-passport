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
    def __init__(self):
        
        self.ALL_SCOPES = {
        "registry.read.operator":"Read Operator data",
        "registry.read.operator_detail":"Read Operator detail data",
        "registry.read.operator_detail.privileged":"Read Operator detail data privileged",
        "registry.read.contact_detail":"Read Contact details",
        "registry.read.contact_detail.privileged":"Read Contact details privileged",
        "registry.read.pilot":"Read Pilot data",
        "registry.read.pilot_detail":"Read Pilot Detail data",
        "registry.read.aircraft":"Read Aircraft data",
        "registry.read.aircraft_detail":"Read Aircraft Detail data",
        "registry.read.aircraft_detail.privileged":"Read Privileged Aircraft data", 
        "dss.read.identification_service_areas":"DSS Read Identification service areas",
        "dss.write.identification_service_areas":"DSS Write Identification service areas",
        "spotlight.write.air_traffic":"Spotlight Write Air traffic Data",
        "spotlight.read.air_traffic":"Spotlight Read Air traffic Data"
    }
        
    def get_all_scopes(self):
        return self.ALL_SCOPES

    def get_available_scopes(self, application=None, request=None, *args, **kwargs):

        if (application.client_class == 1):
            return [ k for k,v in self.ALL_SCOPES.items() if k.startswith('dss.read.')]
            
        elif (application.client_class == 4):
            return [ k for k,v in self.ALL_SCOPES.items() if k.startswith('spotlight.read.')]

        elif (application.client_class == 5):
            return [ k for k,v in self.ALL_SCOPES.items() if k.startswith('spotlight.')]

        else:
            return []

    def get_default_scopes(self, application=None, request=None, *args, **kwargs):
        return []
