from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.


def apptwo_view(request):
    
    return HttpResponse(" this is the apptwo view ")