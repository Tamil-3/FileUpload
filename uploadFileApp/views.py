from django.shortcuts import render, redirect
from django.http import FileResponse
from .models import File

def upload_file(request):
    file = None
    if request.method == 'POST':
        uploaded_file = request.FILES.get('file')
        if uploaded_file:
            file = File.objects.create(name=uploaded_file.name, file=uploaded_file)
    return render(request, 'upload.html', {'file': file})

def download_file(request, file_id):
    file_obj = File.objects.get(id=file_id)
    file_path = file_obj.file.path
    return FileResponse(open(file_path, 'rb'))
