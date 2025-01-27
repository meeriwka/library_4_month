from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models

GENDER = (
    ('M', 'Male'),
    ('F', 'Female'),
)

class UserProfileCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True)
    experience = forms.IntegerField(required=True, label = 'Укажите опыт работы в годах')
    gender = forms.ChoiceField(choices=GENDER, required=True)

    class Meta:
        model = models.UserProfile
        fields = (
            'username',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'experience',
            'gender',
            'phone_number',
        )
    def save(self, commit=True):
        user = super(UserProfileCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.phone_number = self.cleaned_data['phone_number']
        user.experience = self.cleaned_data['experience']
        user.gender = self.cleaned_data['gender']

        if commit:
            user.save()
        return user