from django import forms
from .models import WebAssessmentInfo

class StartWebAssesment(forms.ModelForm):
    class Meta:
        model = WebAssessmentInfo
        fields = ['name','description', 'institute']

