from rest_framework import serializers
from .models import UserProfile, User
from project_info.serializers import Function, PositionSerializer, PositionPostSerializer, FunctionSerializer


class BaseUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'photo', 'position', 'functions', 'about']

    user = BaseUserSerializer()
    position = PositionSerializer()
    functions = FunctionSerializer(many=True)  # serializers.PrimaryKeyRelatedField(queryset=Function.objects.all(), many=True)


class BaseUserPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['first_name', 'last_name']


class UserProfilePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['user', 'position', 'about']

    user = BaseUserPostSerializer()
    position = PositionPostSerializer()


