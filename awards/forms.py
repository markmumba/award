from .models import *
from django import forms

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude=['editor','pub_date']
