from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_profile, name='create_profile'),
    path('profiles/', views.profile_list, name='profile_list'),
    path('profiles/<int:profile_id>/edit/', views.update_profile, name='update_profile'),
    path('profiles/<int:profile_id>/delete/', views.delete_profile, name='delete_profile'),
    path('export/', views.export_profiles, name='export_profiles'),
]
