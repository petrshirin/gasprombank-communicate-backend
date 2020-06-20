from django.shortcuts import render
from rest_framework.views import APIView, Response
from .serializers import *


# Create your views here.
class TechnologyView(APIView):

    def get(self, request):
        technologies = Technology.objects.all()
        ser = TechnologySerializer(technologies, many=True)
        return Response({"data": ser.data}, status=200)


class FunctionView(APIView):

    def get(self, request):
        functions = Function.objects.all()
        ser = FunctionSerializer(functions, many=True)
        return Response({"data": ser.data}, status=200)


class BlockView(APIView):

    def get(self, request):
        blocks = Block.objects.all()
        ser = BlockSerializer(blocks, many=True)
        return Response({"data": ser.data}, status=200)


class PositionView(APIView):

    def get(self, request):
        positions = Position.objects.all()
        ser = PositionSerializer(positions, many=True)
        return Response({"data": ser.data}, status=200)


class DepartmentView(APIView):

    def get(self, request):
        departments = Department.objects.all()
        ser = DepartmentSerializer(departments, many=True)
        return Response({"data": ser.data}, status=200)

