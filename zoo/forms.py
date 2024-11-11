from django import forms
from .models import Animal  

class ChangeEnclosForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['enclos']  
