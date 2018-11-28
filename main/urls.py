from django.conf.urls import url
from .views import (index, AddContainer, reports, viewContainers, addCountry, searchContainers,
                    bookContainer, myBookings, deleteBooking, deleteContainer, confirmBook, confirmArrival)

urlpatterns = [
    url(r'^$', index, name="main"),
    url(r'^reports/$', reports, name="reports"),
    url(r'^search/', searchContainers, name="search"),
    url(r'^book/(?P<cid>[\w]+)/$', bookContainer, name="book"),
    url(r'^view-containers/delete/(?P<cid>[-\w]+)/$', deleteContainer, name="delete-container"),
    url(r'^view-containers/confirm-book/(?P<cid>[-\w]+)/(?P<bid>[-\w]+)/$', confirmBook, name="confirm-book"),
    url(r'^my-bookings/confirm-arrival/(?P<cid>[-\w]+)/(?P<bid>[-\w]+)/$', confirmArrival, name="confirm-arrival"),

    url(r'^book/delete/(?P<bid>[-\w]+)/$', deleteBooking, name="delete"),

    url(r'^my-bookings/$', myBookings, name="my-bookings"),

    url(r'^add-country/$', addCountry, name="add-country"),
    url(r'^add-container/$', AddContainer.as_view(), name="add-container"),
    url(r'^view-containers/$', viewContainers, name="view-containers"),

]
