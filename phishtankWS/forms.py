from django import forms
from models import UploadF


class UploadFileForm(forms.ModelForm):

    class Meta:
        model = UploadF
        fields = ("thumbnail",)