from .models import Todolist
from django import forms

class Taskfom(forms.ModelForm):
    class Meta:
        model = Todolist
        fields=['task', 'done']
