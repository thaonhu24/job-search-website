from django.urls import path
from . import views

urlpatterns = [
      path('post/', views.managePost, name='manage-post'),
      path('applicant/', views.manageApplicant, name='manage-applicant'),
      
]