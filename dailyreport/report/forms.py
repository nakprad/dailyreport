# from django.forms import ModelForm
from django import forms
from .models import Work, Profile, PicWork
import datetime
from bootstrap_datepicker_plus import DatePickerInput
from functools import partial
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout,Field


DateInput = partial(forms.DateInput, {'class': 'datepicker'})

class WorkForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows':3,}))
    # date =  forms.DateField(widget=forms.HiddenInput,)
    # date =  forms.DateField(widget=DateInput(),)
    class Meta:
        model = Work
        fields = ["content"]

    

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    username = forms.TextInput
    first_name = forms.TextInput
    last_name = forms.TextInput
    
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email']

class ProfileUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ['image']

class PicWorkForm(forms.ModelForm):

    pic = forms.ImageField(required=False,label='Select Photo')

    class Meta:
        model = PicWork
        fields = ['pic',]
    
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.layout = Layout(Field('pic'))