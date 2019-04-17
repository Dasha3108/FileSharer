import json
from os import listdir
from os.path import isfile, join

from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    """
        If the request method is GET, renders the page
        Otherwise gets passed file from request
        and saves it to server storage. Returns the rendered page
    """
    if request.method == 'GET':
        return render(request, "index.html")

    my_file = request.FILES['uploaded_file']

    file_system = FileSystemStorage(location=settings.MEDIA_ROOT)
    _ = file_system.save(my_file.name, my_file)

    return render(request, "index.html")


def get_available_files(request):
    """
        Processes only GET request method.
        Returns all files from server storage with their name
        and links to download as json data
    """

    if request.method != 'GET':
        return

    file_system = FileSystemStorage(location=settings.MEDIA_ROOT)

    location = file_system.base_location

    data = []
    for file in listdir(location):
        file_path = join(location, file)

        if isfile(file_path):
            data.append({"file_name": file,
                         "link": settings.MEDIA_URL + file})

    return HttpResponse(json.dumps(data), content_type="application/json")
