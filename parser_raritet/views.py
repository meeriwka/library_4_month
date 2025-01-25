from django.http import HttpResponse
from django.shortcuts import render
from . import forms, models
from django.views import generic

class RaritetListView(generic.ListView):
    template_name = 'parser/raritet_list.html'
    context_object_name = 'raritet'
    model = models.RaritetParser

    def get_queryset(self):
        return self.model.objects.all()

class RaritetFormView(generic.FormView):
    template_name = 'parser/raritet_form.html'
    form_class = forms.ParserForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parser_data()
            return HttpResponse('Parsing is done')
        else:
            return super(RaritetFormView, self).post(request, *args, **kwargs)
