from django import forms
from .models import Schedule



class SGenAppForm(forms.Form):
    #available choices in an array of tuples to add to choicefield args
    INPUT_CHOICES = [
        (5, '5'),
        (10, '10'),
        (15, '15')
    ]
    #created a drop down list to grab arg
    records = forms.ChoiceField(label= 'Records',choices=INPUT_CHOICES)
