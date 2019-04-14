from django.shortcuts import render
from django.http import HttpResponse
import json


def home(request):
    if request.method == 'GET':
        return render(request, "index.html")
    my_file = request.FILES['uploaded_file']

    print(type(my_file))

    return render(request, "index.html")


def get_available_files(request):
    if request.method != 'GET':
        return

    data = [{"file_name": "asd.jpg", "link": "https:/vk.com"}, {"file_name": "lab.docx", "link": "/youtube.com"}]

    return HttpResponse(json.dumps(data), content_type="application/json")
