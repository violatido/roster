from django.http import HttpResponse
import urllib.request
import json
from django.shortcuts import render
from django.http import JsonResponse


def load_roster(request):
    url = "https://coding-assignment.g2crowd.com/"
    page = urllib.request.Request(url,headers={"User-Agent": "Mozilla/5.0"})
    infile = urllib.request.urlopen(page).read().decode()
    data = json.loads(infile)

    context = {"data": data}

    return render(request, 'roster/index.html', context)


