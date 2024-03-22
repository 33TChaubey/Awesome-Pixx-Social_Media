from a_users.models import *
from django import forms
from django.forms import ModelForm


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']
        labels = {
            'realname': 'Name'
        }
        widgets = {
            'image': forms.FileInput(),
            'bio': forms.Textarea(attrs={'rows': 3})
        }


