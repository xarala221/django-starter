from django.conf.urls import url
from myapp.views import *

urlpatterns = [
  url(r"^$", index, name="index")
]