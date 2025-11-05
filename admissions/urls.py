from django.urls import path
from . import views

urlpatterns = [
    path('programs/', views.programs_list, name='programs_list'),
    path('apply/<int:program_id>/', views.apply_for_program, name='apply_for_program'),
    path('my-applications/', views.my_applications, name='my_applications'),
    path('admin/applications/', views.admin_application_list, name='admin_applications'),
    path('admin/applications/update/<int:app_id>/<str:status>/', views.update_application_status, name='update_application_status'),
]
