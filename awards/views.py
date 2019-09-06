from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from .models import *
from django.contrib.auth.decorators import login_required


# Create your views here.
def profile(request):
    current_user = request.user
    profile = Profile.objects.get(id=current_user.id)

    return render(request, 'profile.html', {'profile': profile})


def project(request, project_id):
    try:
        project = Project.objects.get(id=project_id)
    except DoesNotExist:
        raise Http404()
    return render(request, "project.html", {"project": project})


def project_all(request):
   
    projects = Project.print_all()

    return render(request, 'homepg.html', {"projects": projects})
