from django import forms
from . import models


class UrlForm(forms.ModelForm):
    class Meta:
        fields = ("url",)
        model = models.Link
