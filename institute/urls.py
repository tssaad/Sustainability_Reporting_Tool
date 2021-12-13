from django.urls import path
from . import views

app_name = 'institute'

urlpatterns = [
    path('',views.institutes, name='institutes_list'),
    path('<int:id>/',views.institute_detail, name='institute_details'),
    path('add/',views.add_institute, name='add_institute'),
    path('update/<int:id>/',views.update_institute, name='update_institute'),
]
