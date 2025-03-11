

from django import forms
from .models import Visitor

class VisitorForm(forms.ModelForm):
    class Meta:
        model = Visitor
        fields = ['name', 'email', 'purpose_of_visit', 'visit_date']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            'email': forms.EmailInput(attrs={'class': 'form-input'}),
            'purpose_of_visit': forms.Textarea(attrs={'class': 'form-input','rows':'1','columns':'1'}),
            'visit_date': forms.DateInput(attrs={'class': 'form-input'}),
        }
