from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Program, AdmissionApplication
from .forms import AdmissionApplicationForm



@login_required
def programs_list(request):
    programs = Program.objects.select_related('department').all()
    return render(request, 'programs_list.html', {'programs': programs})



@login_required
def apply_for_program(request, program_id):
    program = get_object_or_404(Program, id=program_id)
    if request.method == 'POST':
        form = AdmissionApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.student = request.user
            application.program = program
            application.save()
            messages.success(request, "Your application has been submitted successfully.")
            return redirect('my_applications')
    else:
        form = AdmissionApplicationForm()
    return render(request, 'apply_form.html', {'form': form, 'program': program})


@login_required
def my_applications(request):
    applications = AdmissionApplication.objects.filter(student=request.user)
    return render(request, 'my_applications.html', {'applications': applications})


@login_required
def admin_application_list(request):
    if not request.user.is_staff:
        messages.error(request, "Access Denied.")
        return redirect('dashboard')
    applications = AdmissionApplication.objects.select_related('program', 'student').all()
    return render(request, 'admin_applications.html', {'applications': applications})


@login_required
def update_application_status(request, app_id, status):
    if not request.user.is_staff:
        messages.error(request, "Access Denied.")
        return redirect('dashboard')
    application = get_object_or_404(AdmissionApplication, id=app_id)
    application.status = status
    application.save()
    messages.success(request, f"Application has been {status}.")
    return redirect('admin_applications')

