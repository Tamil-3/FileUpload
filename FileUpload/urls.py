from django.contrib import admin
from django.urls import path
from uploadFileApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload/', views.upload_file, name="upload_file"),
    path('download/<int:file_id>/', views.download_file, name='download_file'),
]
