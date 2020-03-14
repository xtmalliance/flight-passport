from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
# Create your models here.

class UserProfile(models.Model):
    """ User Profile """
    user = models.OneToOneField(User,
                                on_delete= models.CASCADE,
                                unique=True,
                                verbose_name=_('user'),
                                related_name='profile') 
    location = models.CharField(max_length=30, blank=True)
    