from django.conf.urls import url
from .views import index, AddContainer, reports, viewContainers, addCountry

urlpatterns = [
    url(r'^$', index, name="main"),
    url(r'^reports/$', reports, name="reports"),
    url(r'^add-country/$', addCountry, name="add-country"),
    url(r'^add-container/$', AddContainer.as_view(), name="add-container"),
    url(r'^view-containers/$', viewContainers, name="view-containers"),

]
