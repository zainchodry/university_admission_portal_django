from django.db import models
from django.contrib.auth.models import User

class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Program(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='programs')
    name = models.CharField(max_length=100)
    duration_years = models.IntegerField(default=4)
    eligibility = models.TextField()

    def __str__(self):
        return f"{self.name} ({self.department.name})"


APPLICATION_STATUS = (
    ('pending', 'Pending'),
    ('approved', 'Approved'),
    ('rejected', 'Rejected'),
)

class AdmissionApplication(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applications')
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    address = models.TextField()
    transcript = models.FileField(upload_to='transcripts/')
    certificate = models.FileField(upload_to='certificates/')
    applied_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=APPLICATION_STATUS, default='pending')
    admin_remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.full_name} - {self.program.name} ({self.status})"
