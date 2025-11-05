from django import forms
from .models import FacultyProfile, FacultyCourseAssignment, TeachingSchedule


class FacultyProfileForm(forms.ModelForm):
    class Meta:
        model = FacultyProfile
        fields = ['department', 'designation', 'qualification', 'bio', 'profile_image']


class FacultyCourseAssignmentForm(forms.ModelForm):
    class Meta:
        model = FacultyCourseAssignment
        fields = ['faculty', 'course', 'semester', 'year']


class TeachingScheduleForm(forms.ModelForm):
    class Meta:
        model = TeachingSchedule
        fields = ['faculty_course', 'day', 'start_time', 'end_time', 'classroom']
