from django.db import models
from django.contrib.auth.models import User
from admissions.models import Department, Program
from results_and_enrollment.models import Course


class FacultyProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='faculty_profile')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='faculties')
    designation = models.CharField(max_length=100)
    qualification = models.CharField(max_length=200)
    bio = models.TextField(blank=True)
    profile_image = models.ImageField(upload_to='faculty/profile_images/', null=True, blank=True)

    def __str__(self):
        return f"{self.user.get_full_name()} ({self.designation})"


class FacultyCourseAssignment(models.Model):
    faculty = models.ForeignKey(FacultyProfile, on_delete=models.CASCADE, related_name='assigned_courses')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='faculty_assignments')
    semester = models.CharField(max_length=20)
    year = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.faculty.user.get_full_name()} - {self.course.name}"


class TeachingSchedule(models.Model):
    DAYS_OF_WEEK = [
        ('Mon', 'Monday'),
        ('Tue', 'Tuesday'),
        ('Wed', 'Wednesday'),
        ('Thu', 'Thursday'),
        ('Fri', 'Friday'),
        ('Sat', 'Saturday'),
        ('Sun', 'Sunday'),
    ]

    faculty_course = models.ForeignKey(FacultyCourseAssignment, on_delete=models.CASCADE, related_name='schedules')
    day = models.CharField(max_length=3, choices=DAYS_OF_WEEK)
    start_time = models.TimeField()
    end_time = models.TimeField()
    classroom = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.faculty_course.course.name} - {self.day} ({self.start_time} - {self.end_time})"
