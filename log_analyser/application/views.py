from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from . import models

# Create your views here.


def index(request):
    return render(request, 'application/index.html')


def newLog(request):
    if request.method == "POST":
        file_url = request.FILES['fileInput']
        fs = FileSystemStorage()
        filename = fs.save(file_url.name, file_url)
        uploaded_file_url = fs.url(filename)
        #request.session['uploaded_file_url'] = uploaded_file_url
        content = models.read_file(uploaded_file_url)
        context = {'content': content}
    return render(request, 'application/logs.html', context)

def filter(request):
    if request.method == "POST":
        key = request.POST['key']
        uploaded_file_url = request.session['uploaded_file_url']
        content = models.read_file_filter(uploaded_file_url, key)
        context = {'content': content}
    return render(request, 'application/logs.html', context)


