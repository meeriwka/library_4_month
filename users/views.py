from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView
from . import forms, models

class RegisterView(CreateView):
    form_class = forms.UserProfileCreationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

class AuthLoginView(LoginView):
    form_class = forms.AuthenticationForm
    template_name = 'users/login.html'

    def get_success_url(self):
        return reverse_lazy('users:user_list.html')

class AuthLogoutView(LogoutView):
    next_page = reverse_lazy('users:login')

class UserListView(ListView):
    template_name = 'users/user_list.html'
    context_object_name = 'person'
    model = models.UserProfile

    def get_queryset(self):
        return self.model.objects.all()


