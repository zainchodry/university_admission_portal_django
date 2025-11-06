from django.urls import path
from . import views

urlpatterns = [
    path('', views.faculty_dashboard, name='faculty_dashboard'),
    path('create-profile/', views.create_faculty_profile, name='create_faculty_profile'),
    path('assign-course/', views.assign_course, name='assign_course'),
    path('schedule/<int:assignment_id>/', views.manage_schedule, name='manage_schedule'),

    
]
