from django.core.exceptions import ObjectDoesNotExist
from django.db.models.expressions import F
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from project.settings import TIME_ZONE

from .forms import StartWebAssesment

from assessment.models import WebsiteAssessmentDetail, WebAssessmentInfo
from framework.models import Item


def assessment_list(request):
    assessments = WebAssessmentInfo.objects.all()
    context = {
        "assessments" : assessments
    }
    return render(request, 'assessment/assessment_list.html', context)

@login_required
def your_assessment(request):
    assessments = get_object_or_404(WebAssessmentInfo, user=request.user)
    context = {
        "assessments" : assessments
    }
    return render(request, 'assessment/assessment_list.html', context)

def assessment_details(request, id):
    assessment_details = get_object_or_404(WebsiteAssessmentDetail, assessment=id)
    context = {
        'assessment_details' : assessment_details
    }
    return render(request, 'asessment/assessment_details.html', context)


@login_required
def start_web_assessment(request):
    if request.method == "POST":
        form = StartWebAssesment(request.POST)
        if form.is_valid():
            # in case of new assessment
            existing = WebAssessmentInfo.objects.filter(user=request.user, institute=form.cleaned_data['institute'], is_fininshed=False).first()
            if not existing:
                myform = form.save(commit=False)
                myform.user = request.user                
                myform.save()

                current_assessment = WebAssessmentInfo.objects.get(user=request.user, institute=form.cleaned_data['institute'], is_fininshed=False)
                id=current_assessment.id

                message = "A new assessment task has been added!"
                messages.add_message(request, messages.SUCCESS, message)
                auto_add_items(id)
                message = "All items of the assessment framework have automatically been added to your new task. The default value is FALSE to all of them."
                messages.add_message(request, messages.INFO, message)
                
            else: # in case of assessment is going on!
                message = "You have another unfinished task on the same institute. You must complete it first before starting a new task assessment!"
                messages.add_message(request, messages.WARNING, message)
                id = existing.id
            
            return redirect("/assessment/assessment-details/"+str(id) )
        else:
            message = "There is was something wrong in the data provided. Please check it again"
            messages.add_message(request, messages.WARNING, message)
    else:
        form = StartWebAssesment()

    context = {
        'form' : form,
    }
    return render(request, 'assessment/add_web_assessment.html', context)


def auto_add_items(assessment):
    try:
        items = Item.objects.all()
    except ObjectDoesNotExist:
        return False
    for item in items:
        if not WebsiteAssessmentDetail.objects.filter(assessment=assessment, item=item):
            print("+++++++++++++++=")
            newform = WebsiteAssessmentDetail()
            newform.assessment = assessment
            newform.item = item
            newform.created_at = timezone.now()
            newform.updated_at = timezone.now()
            newform.value = False
            newform.save()
    return True
        

