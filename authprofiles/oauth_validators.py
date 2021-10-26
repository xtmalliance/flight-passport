from oauth2_provider.oauth2_validators import OAuth2Validator
   
class PassportOAuth2Validator(OAuth2Validator):
    def get_additional_claims(self, request):
        return {
            "sub": request.user.email,
            "first_name": request.user.first_name,
            "last_name": request.user.last_name,
        }
        
    def get_userinfo_claims(self, request):
        claims = super().get_userinfo_claims()
        return claims


