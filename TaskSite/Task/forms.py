from django import forms
from .models import *
class TaskForm(forms.ModelForm):
    deadline = forms.DateTimeField(widget=forms.DateInput(attrs = {'type':'date'}))
    class Meta:
        model = Task
        fields = ['name','description','receiver','deadline']