from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.decorators import login_required



# Create your views here.
def profile(request):
    current_user = request.user
    profile = Profile.objects.get(id = current_user.id)
   
    return render(request,'profile.html',{'profile':profile})


def project(request, project_id):
    try:
        project = Projects.objects.get(id=project_id)
    except DoesNotExist:
        raise Http404()
    return render(request, "project.html", {"project": project})

