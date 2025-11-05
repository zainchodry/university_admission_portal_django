from django.urls import path
from . import views



urlpatterns = [
    path('dashboard/', views.enrollment_dashboard, name='enrollment_dashboard'),
    path('register-course/', views.register_course, name='register_course'),
    path('results/', views.view_results, name='view_results'),
]
