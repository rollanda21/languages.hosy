from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
#from.models import User


def index(request):
    return render(request, 'index.html')

