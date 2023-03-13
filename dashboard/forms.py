from django.db import models
from .models import UploadWellPictureModel
from django import forms

class UploadWellPictureForm(forms.ModelForm):
    class Meta:
        model = upload_well
        fields = ('picture','name','well_nm','radius','depth','level','village','district','state','pincode', 'lat', 'lng')
