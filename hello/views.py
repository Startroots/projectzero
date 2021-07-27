from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


from .models import Greeting, Job
from .forms import CreatejobForm

import numpy as np
import os

# Create your views here.


def index(request):
    return render(request,'index.html')



def jobs(request):
    # return HttpResponse('Hello from Python!')
    jobs = Job.objects.all()
    return render(request, "jobs.html", {"jobs": jobs})


@login_required(login_url='/login/')
def add(request):
    form_job = CreatejobForm()
    if request.method == 'POST':
        form_job = CreatejobForm(request.POST)
        if form_job.is_valid():
                form_job.save()

    return render(request, "add.html", {"form_job": form_job})

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
