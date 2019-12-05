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


class ContactForm(forms.Form):

    SUBJECTS = (
        ('','--Subject--'),
        ('Request more information','Request more information'),
        ('Learn more about how to contribute','Learn more about how to contribute'),
        ('Correction or bug report','Correction or bug report'),
        ('Other (please specify)','Other (please specify)'),
    )


    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Name',"class":"form-control"}))
    email = forms.EmailField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Email',"class":"form-control"}))
    subject = forms.CharField(max_length=50 ,widget=forms.Select(attrs={'placeholder': 'Subject',"class":"form-control"}, choices=SUBJECTS))
    message = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":30, 'placeholder': 'Message',"class":"form-control different-control w-100"}))
