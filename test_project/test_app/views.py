from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return render(request, 'test_app_site.html')

# def index(request):
#     return HttpResponse("Hello, Django is working!")