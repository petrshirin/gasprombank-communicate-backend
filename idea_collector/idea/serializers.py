from rest_framework import serializers
from .models import *
from user_profile.serializers import UserProfileSerializer
from project_info.serializers import FunctionSerializer, DepartmentSerializer, TechnologySerializer


class IdeaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Idea
        fields = ['id', 'title', 'creator', 'description', 'block', 'functions', 'departments', 'technologies']

    creator = UserProfileSerializer()
    functions = FunctionSerializer(many=True)  # serializers.PrimaryKeyRelatedField(queryset=Function.objects.all(), many=True)
    departments = DepartmentSerializer(many=True)  # serializers.PrimaryKeyRelatedField(queryset=Department.objects.all(), many=True)
    technologies = TechnologySerializer(many=True)  # serializers.PrimaryKeyRelatedField(queryset=Technology.objects.all(), many=True)










