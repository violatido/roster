import urllib.request
import json
from django.shortcuts import render
from django.http import JsonResponse
from roster.models import Employee


def load_roster(request):
    url = "https://coding-assignment.g2crowd.com/"
    page = urllib.request.Request(url,headers={"User-Agent": "Mozilla/5.0"})
    infile = urllib.request.urlopen(page).read().decode()
    data = json.loads(infile)

    employee_names = [e.name for e in Employee.objects.all()]
    employee_data = list() 

    for d in data:
        # If the employee in JSON string has not been made into an Employee object, create employee object
        if d["name"] not in employee_names:
            Employee.objects.create(name=d["name"], title=d["title"], bio=d["bio"], image_url=d["image_url"], vote_count=0)
        # Grab the employee object of all employees in the JSON string, add to employee_data list
        employee_data.append(Employee.objects.get(name=d["name"]))

    context = {"employee_roster": employee_data}

    return render(request, 'roster/index.html', context)


def update_vote_count(request):
    """ Receives a new vote for one specific employee and updates that employee object's vote count.

    The new vote count is returned.
    """
    employee = Employee.objects.get(id=request.GET.get("employee_id"))
    employee.vote_count += 1
    employee.save()

    data = {'success': True, 'vote_count': employee.vote_count}
    return JsonResponse(data)

