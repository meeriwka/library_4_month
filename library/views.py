from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.

def about_me(request):
    if request.method == 'GET':
        return HttpResponse("Hi! I'm Meerim, but my friends call me Meka🥰")

def about_my_pets(request):
    if request.method == 'GET':
        return HttpResponse("I had several puppies and two kittens but my favorite in my memories was the Labrador"
                            "<img src = 'https://labradorretriver.ru/wp-content/uploads/2014/04/golodn-shhenok.png' >")

def date_time(request):
    if request.method == 'GET':
        current_time = datetime.now()
        return HttpResponse(current_time)