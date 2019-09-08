from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import *
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import *


# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    return render(request,'front.html')

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    profile = Profile.objects.get(id=current_user.id)

    return render(request, 'profile.html', {'profile': profile})




@login_required(login_url='/accounts/login/')
def project(request, project_id):
    try:
        project = Project.objects.get(id=project_id)
    except DoesNotExist:
        raise Http404()
    return render(request, "project.html", {"project": project})


@login_required(login_url='/accounts/login/')
def project_all(request):

    projects = Project.print_all()

    return render(request, 'homepg.html', {"projects": projects})


@login_required(login_url='/accounts/login/')
def new_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.editor = current_user
            project.save()
        return redirect('project_all')

    else:
        form = ProjectForm()
    return render(request, 'new_project.html', {"form": form})

class 