from django.shortcuts import render
from .models import IndexPage
from institute.models import Institute
from authentication.models import User

def index(request):
    testmonials = IndexPage.objects.all()
    institutes_list = Institute.objects.all()[0:5]
    num_of_institutes = Institute.objects.all().count()
    candidates = User.objects.all().exclude(is_staff=True, is_superuser=True ) [0:10]

    context = {
        'testmonials':testmonials,
        'num_of_institutes':num_of_institutes,
        'institutes_list':institutes_list,
        'candidates' : candidates,
        }
    return render(request, 'pages/index.html', context)