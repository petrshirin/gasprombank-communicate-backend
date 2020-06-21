from django.shortcuts import render
from .serializers import IdeaSerializer, IdeaPostSerializer, Block, Function, Department, Technology
from rest_framework.views import APIView, Response
from .models import Idea, Like, DisLike


# Create your views here.
class IdeaView(APIView):

    def get(self, request, pk=None):
        if pk:
            idea = Idea.objects.get(pk=pk)
            ser = IdeaSerializer(idea)
            data = ser.data
            return Response(ser.data, status=200)
        else:
            ideas = Idea.objects.all()
            ser = IdeaSerializer(ideas, many=True)
            data = ser.data
            for i in range(len(data)):
                data[i]['likes'] = Like.objects.filter(idea=ideas[i]).count()
                data[i]['dislikes'] = DisLike.objects.filter(idea=ideas[i]).count()
            return Response({'data': ser.data}, status=200)

    def post(self, request):
        data = request.data
        creator = request.user.userprofile
        ser = IdeaPostSerializer(data)

        if ser.is_valid():
            data = ser.validated_data
            data['creator'] = creator
            block = Block.objects.get(pk=data['block'])
            new_idea = Idea(title=data['title'], description=data['description'], creator=creator, block=block)
            new_idea.save()
            
            for pk in data['functions']:
                try:
                    new_idea.functions.add(Function.objects.get(pk=pk))
                except Function.DoesNotExist:
                    return Response({'errors': ['Function does not exist']}, status=422)
            
            for pk in data['department']:
                try:
                    new_idea.functions.add(Department.objects.get(pk=pk))
                except Department.DoesNotExist:
                    return Response({'errors': ['Department does not exist']}, status=422)
                
            for pk in data['technology']:
                try:
                    new_idea.functions.add(Function.objects.get(pk=pk))
                except Function.DoesNotExist:
                    return Response({'errors': ['Technology does not exist']}, status=422)
            new_idea.save()
            return Response({'data': 'ok'}, status=201)



