from django import forms
from .models import Institute
from settings.models import City, Province, Country


class AddInstituteForm(forms.ModelForm):
    class Meta:
        model = Institute
        fields = '__all__'
        exclude = ['created_at', 'updated_at']
    
class UpdateInstituteForm(forms.ModelForm):
    class Meta:
        model = Institute
        fields = '__all__'
        exclude = ['created_at', 'updated_at']
