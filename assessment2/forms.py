from django import forms
from .models import WebAssessmentInfo, WebsiteAssessmentDetail

class StartWebAssesment(forms.ModelForm):
    class Meta:
        model = WebAssessmentInfo
        fields = ['name','description', 'institute']

class WebsiteAssessmentDetailForm(forms.ModelForm):
    class Meta:
        model= WebsiteAssessmentDetail
        fields= '__all__'