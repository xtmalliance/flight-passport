from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
# Create your models here.
from oauth2_provider.models import AbstractApplication

class UserProfile(models.Model):
    """ User Profile """
    user = models.OneToOneField(User,
                                on_delete= models.CASCADE,
                                unique=True,
                                verbose_name=_('user'),
                                related_name='profile') 
    location = models.CharField(max_length=30, blank=True)
    
    
class PassportApplication(AbstractApplication):
    APPLICATION_CLASS_CHOICES = ((0, _('Other')),(1, _('DSS Reader')),(2, _('Registry Reader')),)
    client_class = models.IntegerField(choices=APPLICATION_CLASS_CHOICES,default=0)
    