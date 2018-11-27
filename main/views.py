from django.shortcuts import render, HttpResponse


def index(requeset):
    return HttpResponse('hello world this is LBEF CMS :D')
