from django.shortcuts import render
from .serializers import IdeaSerializer
from rest_framework.views import APIView, Response
from .models import Idea


# Create your views here.
class IdeaView(APIView):

    def get(self, request, pk=None):
        if pk:
            idea = Idea.objects.get(pk=pk)
            ser = IdeaSerializer(idea)
            return Response(ser.data, status=200)
        else:
            ideas = Idea.objects.all()
            ser = IdeaSerializer(ideas, many=True)
            return Response({'data': ser.data}, status=200)




