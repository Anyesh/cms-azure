from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.views import View
from .forms import AddContainerForm, AddCountryForm
from django.urls import reverse
from django.contrib import messages
from .models import Container, Country, Booking
import datetime

def index(request):
    data = Country.objects.all()
    return render(request, 'main/index.html', {"data": data})


def addCountry(request):
    if request.method == 'POST':
        form = AddCountryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Country added successfully.')
            return HttpResponseRedirect(reverse('add-container'))
        else:
            messages.error(request, 'There was an error!!')
            return HttpResponseRedirect(reverse('add-container'))
    else:
        form = AddCountryForm(None)
        ctx = {"form": form}
        return render(request, 'container/addCountry.html', ctx)



class AddContainer(View):

    def get(self, request):
        form = AddContainerForm(None)
        ctx = {"form": form}
        return render(request, 'container/add.html', ctx)

    def post(self, request):
        form = AddContainerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Container added successfully.')
            return HttpResponseRedirect(reverse('add-container'))
        else:
            messages.error(request, 'Container ID Should be unique. Choose different one.')
            return HttpResponseRedirect(reverse('add-container'))


def viewContainers(request):
    containers = Container.objects.all()
    ctx = {"containers": containers}
    return render(request, 'container/view.html', ctx)



def reports(request):
    from_date = request.GET.get('from')
    to_date = request.GET.get('to')
    if from_date and to_date:
        bookings = Booking.objects.filter(timestamp__date__range=[from_date, to_date])
        return render(request, 'reports/index.html', {'bookings': bookings})
    else:
        return render(request, 'reports/index.html')




def searchContainers(request):
    data = Country.objects.all()
    country = request.GET.get('country')
    print(country)
    containers = Container.objects.filter(country__title=country, available=True)
    ctx = {"data": data, 'containers': containers}
    return render(request, 'search/results.html', ctx)


def myBookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'bookings/index.html', {'bookings': bookings})


def bookContainer(request, cid):
    user = request.user
    if not user:
        messages.error(request, 'Not a valid user!')
        return HttpResponseRedirect(reverse('search'))

    container = Container.objects.get(cid=cid)
    if not container:
        messages.error(request, 'Not a valid container!')
        return HttpResponseRedirect(reverse('search'))

    _, created = Booking.objects.get_or_create(user=user, container=container,
                                            location=request.user.profile.country)

    container.available = False
    container.save()
    messages.success(request, 'Container Booked!')
    return HttpResponseRedirect(reverse('search'))


def deleteContainer(request, cid):
    if request.user.is_superuser:
        container = Container.objects.get(cid=cid)
        container.delete()
        messages.success(request, 'Container Deleted!')
        return HttpResponseRedirect(reverse('view-containers'))
    else:
        messages.error(request, 'Not Authorized to Delete!')
        return HttpResponseRedirect(reverse('view-containers'))


def confirmBook(request, cid, bid):
    if request.user.is_superuser:
        container = Container.objects.get(cid=cid)
        booking = Booking.objects.get(bid=bid)
        booking.departure_date = datetime.datetime.now()
        booking.save()
        container.departed = True
        container.save()
        messages.success(request, 'Booking confirmed and Container departed!')
        return HttpResponseRedirect(reverse('view-containers'))
    else:
        messages.error(request, 'There was an error!')
        return HttpResponseRedirect(reverse('view-containers'))


def confirmArrival(request, cid, bid):
    booking = Booking.objects.get(bid=bid)
    if request.user == booking.user:
        container = Container.objects.get(cid=cid)
        booking.arrival_date = datetime.datetime.now()
        booking.save()
        container.received = True
        container.save()
        messages.success(request, 'Arrival confirmed !')
        return HttpResponseRedirect(reverse('my-bookings'))
    else:
        messages.error(request, 'There was an error!')
        return HttpResponseRedirect(reverse('my-bookings'))



def deleteBooking(request, bid):
    booking = Booking.objects.get(bid=bid)
    if booking.user == request.user:
        print(booking.container)
        container = Container.objects.get(cid=booking.container)
        container.available = True
        container.save()
        booking.delete()
        messages.success(request, 'Booking Deleted!')
        return HttpResponseRedirect(reverse('my-bookings'))
    else:
        messages.error(request, 'Error!!!')
        return HttpResponseRedirect(reverse('my-bookings'))






