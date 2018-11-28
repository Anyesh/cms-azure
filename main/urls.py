from django.conf.urls import url
from .views import index, AddContainer, reports, viewContainers, addCountry, searchContainers, bookContainer, myBookings

urlpatterns = [
    url(r'^$', index, name="main"),
    url(r'^reports/$', reports, name="reports"),
    url(r'^search/', searchContainers, name="search"),
    url(r'^book/(?P<cid>[\w]+)/', bookContainer, name="book"),
    url(r'^my-bookings/$', myBookings, name="my-bookings"),

    url(r'^add-country/$', addCountry, name="add-country"),
    url(r'^add-container/$', AddContainer.as_view(), name="add-container"),
    url(r'^view-containers/$', viewContainers, name="view-containers"),

]
