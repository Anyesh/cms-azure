from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.views import View
from .forms import AddContainerForm
from django.urls import reverse
from django.contrib import messages
from .models import Container

def index(request):
    return render(request, 'main/index.html')


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
            messages.success(request, 'Container ID Should be unique. Choose different one.')
            return HttpResponseRedirect(reverse('add-container'))


def viewContainers(request):
    containers = Container.objects.all()
    ctx = {"containers": containers}
    return render(request, 'container/view.html', ctx)



def bookings(request):
    return render(request, 'bookings/index.html')
