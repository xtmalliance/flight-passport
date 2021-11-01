from django.conf.urls import url
from .views import SignView

app_name = "jws_helper"

urlpatterns = [
    url(r"^sign/$", SignView.as_view(), name="sign"),
    
]
