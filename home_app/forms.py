from django import forms
from .models import BookTable

class BookTableForm(forms.ModelForm):
    class Meta:
        model = BookTable
        fields = ['name','number', 'email', 'person', 'date']
