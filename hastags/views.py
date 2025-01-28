from django.shortcuts import render
from . import models


#общий список продуктов
def all_products(request):
    if request.method == 'GET':
        all_products = models.Product.objects.all()
        context = {'all_products': all_products}
        return render(request, template_name='hastags/all_products.html',
                      context=context)

#список  сказок
def fairy_tales(request):
    if request.method == 'GET':
        fairy_tales = models.Product.objects.filter(tags__name='Сказки')
        context = {'fairy_tales': fairy_tales}
        return render(request, template_name='hastags/fairy_tales.html',
                      context=context)

#список фантастики
def fantasy(request):
    if request.method == 'GET':
        fantasy = models.Product.objects.filter(tags__name='Фантастика')
        context = {'fantasy': fantasy}
        return render(request, template_name='hastags/fantasy.html',
                      context=context)

#список драмы
def drama(request):
    if request.method == 'GET':
        drama = models.Product.objects.filter(tags__name='Драма')
        context = {'drama': drama}
        return render(request, template_name='hastags/drama.html',
                      context=context)


