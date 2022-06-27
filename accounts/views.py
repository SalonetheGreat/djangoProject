from django.http import HttpResponse, Http404
from django.shortcuts import render


def index(request):
    if request.method == 'GET':
        return render(request, 'accounts/index.html')
    elif request.method == 'POST':
        return HttpResponse('We have received a POST request @index')
    else:
        raise Http404()


def login(request):
    if request.method == 'GET':
        return render(request, 'accounts/login.html')
    elif request.method == 'POST':
        return HttpResponse('We have received a POST request @login')
    else:
        raise Http404()


def logout(request):
    if request.method == 'POST':
        return HttpResponse('We have received a POST request @logout')
    else:
        raise Http404()


def register(request):
    if request.method == 'GET':
        return render(request, 'accounts/register.html')
    elif request.method == 'POST':
        return HttpResponse('We have received a POST request @register')
    else:
        raise Http404()


