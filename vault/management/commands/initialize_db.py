from django.core.management.base import BaseCommand, CommandError
# from plcnxdb.db.models import BOMConfig, PolicyConfig #,analysisProductPlans,storageProductPlans
from django.contrib.sites.models import Site
from django.conf import settings as settings


class Command(BaseCommand):
    # args = '<user_name>'
    help = 'Initiailizes database and site in Django'

    def handle(self, *args, **options):
        print("Setting site name and domain")
        site = Site.objects.get(id=1)
        
        site.name = settings.JWT_ISSUER
        site.domain =settings.JWT_ISSUER_DOMAIN
        site.save()