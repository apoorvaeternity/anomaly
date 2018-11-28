from django import forms
from django.forms import Form


class FileUploadForm(Form):
    file = forms.FileField(label='Select a CSV file', widget=forms.FileInput(attrs={'accept':'.csv'}))
