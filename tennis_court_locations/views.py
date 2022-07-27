from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, 'home.html', {})

# def home_view(request, *args, **kwargs):
#     return HttpResponse("<h1>Hello World!</h1>")

def test_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request)
    print(request.user)
    return HttpResponse("<h1>Test!</h1>")

def about_view(request, *args, **kwargs):
    my_context = {
        "my text" : "This is about us"
    }
    return render(request, 'home.html', {})