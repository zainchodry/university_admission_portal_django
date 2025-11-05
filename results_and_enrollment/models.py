from django.db import models
from django.contrib.auth.models import User
from admissions.models import Program


class Enrollment(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='enrollments')
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    enrollment_date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.student.username} - {self.program.name}"


class Course(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='courses')
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=200)
    credit_hours = models.PositiveIntegerField(default=3)

    def __str__(self):
        return f"{self.code} - {self.name}"


class RegisteredCourse(models.Model):
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE, related_name='registered_courses')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    semester = models.CharField(max_length=20)
    year = models.PositiveIntegerField()
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.enrollment.student.username} - {self.course.name}"


class Result(models.Model):
    registered_course = models.OneToOneField(RegisteredCourse, on_delete=models.CASCADE, related_name='result')
    marks_obtained = models.FloatField()
    grade = models.CharField(max_length=2)
    gpa = models.FloatField()

    def __str__(self):
        return f"{self.registered_course.course.name} - {self.grade}"
