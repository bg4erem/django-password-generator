from operator import le
from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def password(request):
    len = int(request.GET.get('length', 12))
    characters = list('abcdefghijklmnopqrstuvwxyz')
    thepassword = ''

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('#%$*!@()-+'))
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))

    for x in range(len):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password':thepassword})

def about(request):
    return render(request, 'generator/about.html')