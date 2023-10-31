from django import forms 
from .models import Todo 
class TodoRegistration(forms.ModelForm):
    class Meta:
          model=Todo
          fields=['task','completed']
        
  