from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from institute.models import Institute
from settings.models import City, Country, Province

from .forms import AddInstituteForm, UpdateInstituteForm

def institutes(request):
    institutes_list = Institute.objects.all()
    num_of_institutes = institutes_list.count()
    paginator = Paginator(institutes_list, 5) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)    

    context = {
        'institutes_list': page_obj, 
        'num_of_institutes':num_of_institutes,
    }
    return render(request, 'institute/institutes.html', context)

def institute_detail(request, id):
    institute = Institute.objects.get(id=id)
    context = {
        'institute' : institute,
    }
    return render(request, 'institute/institute_details.html', context)

@login_required
def add_institute(request):
    if request.method == "POST":
        form = AddInstituteForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            message = "The institute has been added sucessfully!"
            messages.add_message(request, messages.INFO, message)
            return redirect(reverse("institute:institutes_list"))
        else:
            message = "There was something wrong, please double check your entried data!"
            messages.add_message(request, messages.INFO, message)
    else:
        form = AddInstituteForm()
    
    context = {'form' : form }
    return render(request, 'institute/add_institute.html', context)

@login_required
def update_institute(request, id):
    instance = Institute.objects.get(id=id)
    if request.method == "POST":
        form = UpdateInstituteForm(request.POST or None, request.FILES or None, instance=instance)
        if form.is_valid():
            form.save()
            message = "The institute has been updated sucessfully!"
            messages.add_message(request, messages.SUCCESS, message)
            return redirect("/institute/"+str(id))
        else:
            message = "There was something wrong, please double check your entried data!"
            messages.add_message(request, messages.WARNING, message)
    else:
        form = UpdateInstituteForm(instance=instance)

    context = {'form':form}
    return render(request, 'institute/update_institute.html', context)

