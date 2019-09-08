from rest_framework import serializers
from .models import *


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:

        model = Profile
        fields = ('id','profile_photo','user','projects')


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:

        model = Project
        fields= ('id','title','links','description')