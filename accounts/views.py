from django.shortcuts import render, redirect
from . models import *
from . forms import *
from django.contrib import messages
from django.contrib.auth import logout as auth_logout





def register_view(request):
    if request.method == 'POST':
        user_form = RegisterForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit = False)
            user.save()
            profile = profile_form.save(commit = False)
            profile.user = user
            profile.save()
            messages.success(request, "Register Successfull Please Login")
            return redirect('login')
        
    else:
        user_form = RegisterForm()
        profile_form = ProfileForm()
    return render(request, "register.html", {"user_form":user_form, "profile_form":profile_form})





def logout(request):
    auth_logout(request)
    messages.success(request, "Logout Successfull")
    return redirect('login')




def dashboard_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    profile = Profile.objects.get(user=request.user)
    return render(request, 'dashboard.html', {'profile': profile})



