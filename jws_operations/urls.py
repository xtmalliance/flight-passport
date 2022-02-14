from django.urls import re_path
from .views import SignView

app_name = "jws_helper"

urlpatterns = [
    re_path(r"^sign/$", SignView.as_view(), name="sign"),
    
]
