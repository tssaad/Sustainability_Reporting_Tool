from django.urls import path
from . import views

app_name = 'assessment'

urlpatterns = [
    path('start-web-assessment/',views.start_web_assessment, name="start_web_assessment"),
    path('assessment-list/',views.assessment_list, name="assessment_list"),
    path('your-assessment/',views.your_assessment, name="your_assessment"),
    path('assessment-details/<int:id>',views.assessment_details, name="assessment_details"),
]
