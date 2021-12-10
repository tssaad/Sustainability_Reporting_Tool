from django.shortcuts import render
from institute.models import Institute

def institutes(request):
    institutes_list = Institute.objects.all()
    count = institutes_list.count()
    context = {
        'institutes_list': institutes_list,  
        'count' : count,
    }
    return render(request, 'institute/institutes.html', context)

def institute_detail(request, id):
    institute = Institute.objects.get(id=id)
    context = {
        'institute' : institute,
    }
    return render(request, 'institute/institute_details.html', context)