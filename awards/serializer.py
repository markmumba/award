from rest_framework import serializers
from .models import *


class ProfileSerializer(serializers.ModelSerializer):
    model = Profile
    fields = ('profile_photo',' user_bio','user,projects')


class ProjectSerializer(serializers.ModelSerializer):
    model = Project
    fields= ('title','links','description')