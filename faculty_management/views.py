from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import FacultyProfile, FacultyCourseAssignment, TeachingSchedule
from .forms import FacultyProfileForm, FacultyCourseAssignmentForm, TeachingScheduleForm


# 🧑‍🎓 Faculty Dashboard
@login_required
def faculty_dashboard(request):
    profile = FacultyProfile.objects.filter(user=request.user).first()
    assignments = FacultyCourseAssignment.objects.filter(faculty=profile)
    return render(request, 'faculty_management/faculty_dashboard.html', {
        'profile': profile,
        'assignments': assignments
    })


# 🧑‍🏫 Create/Update Faculty Profile
@login_required
def create_faculty_profile(request):
    if request.method == 'POST':
        form = FacultyProfileForm(request.POST, request.FILES)
        if form.is_valid():
            faculty = form.save(commit=False)
            faculty.user = request.user
            faculty.save()
            messages.success(request, "Profile created successfully.")
            return redirect('faculty_dashboard')
    else:
        form = FacultyProfileForm()
    return render(request, 'faculty_management/faculty_profile_form.html', {'form': form})


# 📚 Assign Courses to Faculty (Admin only)
@login_required
def assign_course(request):
    if not request.user.is_staff:
        messages.error(request, "Access Denied. Admins only.")
        return redirect('faculty_dashboard')

    if request.method == 'POST':
        form = FacultyCourseAssignmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Course assigned successfully.")
            return redirect('faculty_dashboard')
    else:
        form = FacultyCourseAssignmentForm()
    return render(request, 'faculty_management/assign_course.html', {'form': form})


# 🗓️ Manage Teaching Schedule
@login_required
def manage_schedule(request, assignment_id):
    assignment = get_object_or_404(FacultyCourseAssignment, id=assignment_id)
    schedules = TeachingSchedule.objects.filter(faculty_course=assignment)

    if request.method == 'POST':
        form = TeachingScheduleForm(request.POST)
        if form.is_valid():
            schedule = form.save(commit=False)
            schedule.faculty_course = assignment
            schedule.save()
            messages.success(request, "Schedule added successfully.")
            return redirect('manage_schedule', assignment_id=assignment.id)
    else:
        form = TeachingScheduleForm()

    return render(request, 'faculty_management/manage_schedule.html', {
        'assignment': assignment,
        'form': form,
        'schedules': schedules
    })
