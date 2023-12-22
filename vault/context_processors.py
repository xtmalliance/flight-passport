from django.conf import settings


def from_settings(request):
    kwargs = {
        "logo_url": settings.LOGO_URL,
        "application_name": settings.APPLICATION_NAME,
        "domain_name": settings.JWT_ISSUER_DOMAIN,
    }
    return kwargs
