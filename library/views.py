from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from . import models

#список книг
def book_list(request):
    if request.method == "GET":
        book_list = models.Books.objects.all().order_by('-id')
        context = {'book_list': book_list}
        return render(request, template_name='book.html', context=context)

def book_detail(request, id):
    if request.method == "GET":
        book_id = get_object_or_404(models.Books, id=id)
        context = {'book_id': book_id}
        return render(request, template_name='book_detail.html', context=context)










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