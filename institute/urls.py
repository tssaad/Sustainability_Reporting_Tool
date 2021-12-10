from django.urls import path
from . import views

app_name = 'institute'

urlpatterns = [
    path('',views.institutes, name='institutes_list'),
    path('<int:id>',views.institute_detail, name='institute_details'),
]
