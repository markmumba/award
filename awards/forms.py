from .models import *
from django import forms

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude=['editor','pub_date']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['prof_user','profile_Id']

