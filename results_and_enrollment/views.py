from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Enrollment, RegisteredCourse, Result, Course
from .forms import CourseRegistrationForm
from admissions.models import Program

@login_required
def enrollment_dashboard(request):
    enrollments = Enrollment.objects.filter(student=request.user)
    return render(request, 'enrollment_dashboard.html', {'enrollments': enrollments})


@login_required
def register_course(request):
    enrollment = Enrollment.objects.filter(student=request.user, is_active=True).first()

    if not enrollment:
        messages.warning(request, "You must be enrolled in a program first.")
        return redirect('enrollment_dashboard')

    if request.method == 'POST':
        form = CourseRegistrationForm(request.POST)
        if form.is_valid():
            reg_course = form.save(commit=False)
            reg_course.enrollment = enrollment
            reg_course.save()
            messages.success(request, "Course registered successfully!")
            return redirect('enrollment_dashboard')
    else:
        form = CourseRegistrationForm()

    return render(request, 'register_course.html', {'form': form})


@login_required
def view_results(request):
    results = Result.objects.filter(registered_course__enrollment__student=request.user)
    return render(request, 'view_results.html', {'results': results})
