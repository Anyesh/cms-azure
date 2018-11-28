from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.views import View
from .forms import AddContainerForm, AddCountryForm
from django.urls import reverse
from django.contrib import messages
from .models import Container, Country, Booking

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
    return render(request, 'reports/index.html')


def searchContainers(request):
    data = Country.objects.all()
    country = request.GET.get('country')
    print(country)
    containers = Container.objects.filter(country__title=country)
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

    _, created = Booking.objects.get_or_create(user=user, container=container)
    if not created:
        container.available = False
        container.save()
        messages.success(request, 'Container Booked!')
        return HttpResponseRedirect(reverse('search'))
    else:
        messages.error(request, 'Container Unavailable!')
        return HttpResponseRedirect(reverse('search'))




