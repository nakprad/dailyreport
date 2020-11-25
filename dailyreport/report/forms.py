# from django.forms import ModelForm
from django import forms
from .models import Work
import datetime
from bootstrap_datepicker_plus import DatePickerInput
from functools import partial
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

DateInput = partial(forms.DateInput, {'class': 'datepicker'})

class WorkForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea)
    date =  forms.DateField(widget=DateInput())

    class Meta:
        model = Work
        fields = ["date","content","update_at"]

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']