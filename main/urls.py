from django.conf.urls import url
from .views import index, AddContainer, bookings, viewContainers

urlpatterns = [
    url(r'^$', index, name="main"),
    url(r'^bookings/', bookings, name="bookings"),

    url(r'^add-container/', AddContainer.as_view(), name="add-container"),
    url(r'^view-containers/', viewContainers, name="view-containers"),

]
