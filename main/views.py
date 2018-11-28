from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.views import View
from .forms import AddContainerForm, AddCountryForm
from django.urls import reverse
from django.contrib import messages
from .models import Container

def index(request):
    return render(request, 'main/index.html')


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
