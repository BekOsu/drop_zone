from django.urls import path
from .import views

urlpatterns = [
    path('',views.Home.as_view(),name='home'),
    path('upload',views.file_upload,name='upload-file'),
]
