from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(label="Email", required=True)

    class Meta:
        model = get_user_model()
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class OtterSelection(forms.Form):
    ottname = forms.ModelChoiceField(
        label="Select an Otter!",
        queryset=models.onsite.objects.all(),
        required=True,
    )
