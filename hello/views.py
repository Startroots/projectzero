from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


from .models import Greeting, Job
from .forms import CreatejobForm

import numpy as np
import os

# Create your views here.



def index(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join(BASE_DIR, 'static/img/occupation/png')

    filenames = os.listdir(path)
    filenames = np.array(filenames) #transform to numpy array
    filenames = np.random.permutation(filenames) #positions permutations
	
    files = []
    for i in range(len(filenames)):
	    files.append('img/occupation/png/'+filenames[i])

    files = files[:5] #return de first fives

    return render(request,'index.html', {"files":files})



def jobs(request):
    # return HttpResponse('Hello from Python!')
    job = Job()
    job.save()

    jobs = Job.objects.all()
    return render(request, "jobs.html", {"jobs": jobs})

url="https://intercambiapp.herokuapp.com/"

@login_required(login_url=url+'login')
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
