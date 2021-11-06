from django.urls import path
from . import views

urlpatterns = [
      path('listjob/', views.listJob, name='list-job'),
      path('detail/', views.detailJob, name='detail-job'),
      path('add-post/', views.addNewPost, name='add-new-post'),
      path('add-post/search/', views.search_result, name='search'),
      path('add-post/add-skill/', views.add_skill, name='add-skill'),
      path('save/', views.savePost, name='save'),
]