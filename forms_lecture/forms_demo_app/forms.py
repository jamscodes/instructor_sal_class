from django import forms
from .models import *
from .validators import *

class First_Form(forms.Form):
    f_name = forms.CharField(label = 'Your name', max_length=100, error_messages={'required': 'Please enter your first name.'})
    not_required = forms.CharField(max_length=100, required=False)

class DB_Form(forms.ModelForm):
    class Meta:
        model = User
        fields = ['f_name','l_name','fav_instrument', 'rock']
        labels = {
            'rock': 'Do you like to rock?'
        }