from django.shortcuts import redirect, render, reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from authentication.models import User
from .forms import ProfileEditForm, SignupForm

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()

            user = authenticate(email=form.cleaned_data['email'], password=form.cleaned_data['password1'])
            login(request, user)

            message = "Your Profile has been updated sucessfully!"
            messages.add_message(request, messages.INFO, message)            
            return redirect(reverse("accounts:profile"))
        else:
            message="Somthing Worng happened. Please check your data."
            messages.add_message(request, messages.INFO, message)                        
    else:
        form = SignupForm()
    context = {'form' : form}
    return render(request, 'registration/signup.html', context)

@login_required
def profile(request):
    profile = User.objects.get(email=request.user)
    context = {
        'profile': profile
    }

    return render(request,'accounts/profile.html', context)

@login_required
def profile_edit(request):
    #profile = User.objects.get(email=request.user)

    if request.method == "POST":
        form = ProfileEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            message = "Your Profile has been updated sucessfully!"
            messages.add_message(request, messages.INFO, message)            
            return redirect(reverse("accounts:profile"))
        else:
            message = "Something went wrong, please check the data again!"
            messages.add_message(request, messages.INFO, message)                        
    else:
        form = ProfileEditForm(instance=request.user)

    context = {
        'form' : form,
    }
    return render(request, 'accounts/profile_edit.html', context)

