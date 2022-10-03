from django import forms
from .models import todos

class todosForm(forms.ModelForm):
    class Meta:
        model = todos
        fields = ['title', 'discription']