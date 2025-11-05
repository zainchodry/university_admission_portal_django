from django import forms
from .models import AdmissionApplication



class AdmissionApplicationForm(forms.ModelForm):
    class Meta:
        model = AdmissionApplication
        exclude = ['student', 'status', 'applied_date', 'admin_remarks']
