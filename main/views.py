from django.shortcuts import render, HttpResponse


def index(requeset):
    return render(requeset, 'main/index.html')
