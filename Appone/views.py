from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def appone_view(request):

    return HttpResponse(' this is appone view ')


