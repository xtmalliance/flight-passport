from django.conf import settings
from oauth2_provider.oauth2_validators import OAuth2Validator

from oauth2_provider_jwt.utils import encode_jwt


class PassportOAuth2Validator(OAuth2Validator):
    def get_additional_claims(self, request):
        groups = []
        for g in request.user.groups.all():
            groups.append(g.name)

        return {"email": request.user.email, "role": " ".join(groups)}

    def get_userinfo_claims(self, request):
        claims = super().get_userinfo_claims(request)

        return claims
