from django.conf.urls import url
from .views import index,getnews

urlpatterns = [
    url(r'^$', index,name="index"),
    url(r'^getnews/$', getnews, name="getnews")

]
