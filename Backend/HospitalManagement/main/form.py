from django import forms
from .models import Nurse


class ImageUpload(forms.ModelForm):

    class Meta:
        model = Nurse
        fields = ['name', 'profile_pic']
