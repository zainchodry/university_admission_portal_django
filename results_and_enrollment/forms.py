from django import forms
from .models import RegisteredCourse



class CourseRegistrationForm(forms.ModelForm):
    class Meta:
        model = RegisteredCourse
        fields = ['course', 'semester', 'year']
