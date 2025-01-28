from django.shortcuts import render, redirect, get_object_or_404
from . import models, forms

def create_basket_view(request):
    if request.method == "POST":
        form = forms.BasketForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('basket_list')
    else:
        form = forms.BasketForm()
    return render(request, template_name='basket/create_basket.html', context={'form': form})


def basket_list_view(request):
    if request.method == "GET":
        basket_list = models.Basket.objects.all().order_by('-id')
        context = {'basket_list': basket_list}
        return render(request, template_name='basket/basket_list.html', context=context)


def basket_detail_view(request, id):
    if request.method == "GET":
        basket_id = get_object_or_404(models.Basket, id=id)
        context = {'basket_id': basket_id}
        return render(request, template_name='basket/basket_detail.html', context=context)
