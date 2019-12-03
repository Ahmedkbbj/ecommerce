from django.forms import ModelForm
from django import forms
from .models import Client
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
class ClientForm(forms.ModelForm):
    

    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)
        self.fields['age'].widget.attrs['class'] = 'form-control'
        self.fields['age'].widget.attrs['placeholder'] = 'Age'

    class Meta:


        model = Client
        exclude = ('created_at',)

        widgets = {
                'first_name': forms.TextInput(attrs={'placeholder': 'First Name',"class":"form-control"}),
                'last_name': forms.TextInput(attrs={'placeholder': 'Last Name', "class":"form-control"}),
                'email': forms.TextInput(attrs={'placeholder': 'Email', "class":"form-control"}),
                'phone': forms.TextInput(attrs={'placeholder': 'Phone', "class":"form-control"}),
                'adress': forms.TextInput(attrs={'placeholder': 'Adress', "class":"form-control"}),
                'city': forms.TextInput(attrs={'placeholder': 'City', "class":"form-control"}),
                'gender': forms.Select(attrs={'placeholder': 'Sex', 'class': 'form-control'}),
                'country': CountrySelectWidget(
                    attrs={"placeholder":"select country","class": "form-control"}
                )
            }
    