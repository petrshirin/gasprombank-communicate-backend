from rest_framework import serializers
from .models import Technology, Function, Block, Position, Department


class TechnologySerializer(serializers.ModelSerializer):

    class Meta:
        model = Technology
        fields = ['id', 'name']


class FunctionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Function
        fields = ['id', 'name']


class BlockSerializer(serializers.ModelSerializer):

    class Meta:
        model = Block
        fields = ['id', 'name']


class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = ['id', 'name']


class PositionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Position
        fields = ['id', 'name', 'department']

    department = DepartmentSerializer()


class PositionPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ['id']

