from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import *
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import *
from .permission import IsAdminOrReadOnly


# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    return render(request, 'front.html')


@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    profile = Profile.objects.get(id=current_user.id)

    return render(request, 'profile.html', {'profile': profile})


@login_required(login_url='/accounts/login/')
def create_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.username = current_user

            profile.save()
        return redirect('index')
    else:
        form = ProfileForm()

    return render(request, 'new_profile.html', {"form": form})


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


class ProfileList(APIView):
    def get(self, request, format=None):
        all_profiles = Profile.objects.all()
        serializers = ProfileSerializer(all_profiles, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = ProfileSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    permission_classes = (IsAdminOrReadOnly,)


class Projectlist(APIView):
    def get(self, request, format=None):
        projects = Project.objects.all()
        serializers = ProjectSerializer(projects, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = ProjectSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    permission_classes = (IsAdminOrReadOnly,)


class ProfileDes(APIView):
    permission_classes = (IsAdminOrReadOnly,)

    def get_profile(self, pk):
        try:
            return Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        prof = self.get_profile(pk)
        serializers = ProfileSerializer(prof)
        return Response(serializers.data)

    def put(self, request, pk, format=None):
        prof = self.get_profile(pk)
        serializers = ProfileSerializer(prof, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        prof = self.get_profile(pk)
        prof.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProjectDes(APIView):
    permission_classes = (IsAdminOrReadOnly,)

    def get_project(self, pk):
        try:
            return Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        proj = self.get_project(pk)
        serializers = ProjectSerializer(proj)
        return Response(serializers.data)

    def put(self, request, pk, format=None):
        proj = self.get_project(pk)
        serializers = ProjectSerializer(proj, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        proj = self.get_project(pk)
        proj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
