import json
from os import listdir
from os.path import isfile, join, relpath

from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render

FILES_FOLDER = 'uploaded_files/'


def home(request):
    if request.method == 'GET':
        return render(request, "index.html")
    my_file = request.FILES['uploaded_file']

    file_system = FileSystemStorage(location=FILES_FOLDER)
    _ = file_system.save(my_file.name, my_file)

    return render(request, "index.html")


def get_available_files(request):
    if request.method != 'GET':
        return

    file_system = FileSystemStorage(location=FILES_FOLDER)

    location = file_system.base_location

    data = []
    for file in listdir(location):
        file_path = join(location, file)
        if isfile(file_path):
            print(relpath(file, settings.MEDIA_ROOT))

            data.append({"file_name": file,
                         "link": "/media/" + file})

    return HttpResponse(json.dumps(data), content_type="application/json")
