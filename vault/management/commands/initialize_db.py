from django.core.management.base import BaseCommand, CommandError
# from plcnxdb.db.models import BOMConfig, PolicyConfig #,analysisProductPlans,storageProductPlans
from django.contrib.sites.models import Site

class Command(BaseCommand):
    # args = '<user_name>'
    help = 'Initiailizes database and site in Django'

    def handle(self, *args, **options):
        print("Setting site name")
        site = Site.objects.get(id=1)
        
        site.name = 'Openskies ID'
        site.domain ='id.openskies.sh'
        site.save()