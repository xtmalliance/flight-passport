from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
# Create your models here.
from oauth2_provider.models import AbstractApplication
import uuid


class PassportScope(models.Model):
    uuid = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    name = models.CharField(max_length=140, help_text='e.g. dss.read.identification_service_areas')
    description = models.CharField(max_length=140)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()
    def __uniode__(self):
        return self.__str__()

    
class PassportAPI(models.Model):
    uuid = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    identifier = models.CharField(max_length=140, help_text='e.g. che.openskies.sh')
    name = models.CharField(max_length=140)
    scopes = models.ManyToManyField(PassportScope, related_name = 'api_scope', blank = True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()
    def __uniode__(self):
        return self.__str__()


class PassportApplication(AbstractApplication):
    APPLICATION_CLASS_CHOICES = ((0, _('Other')),(1, _('Remote ID Display Provider')),(2, _('Registry Reader')),(3, _('Login only')),(4, _('Flight Spotlight Reader')),(5, _('Flight Spotlight Writer')),(6, _('Remote ID Service Provider')),)
    client_class = models.IntegerField(choices=APPLICATION_CLASS_CHOICES,default=0)
    audience = models.ManyToManyField(PassportAPI, related_name = 'application_audience', blank=True)    
    