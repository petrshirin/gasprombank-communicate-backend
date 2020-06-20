from django.shortcuts import render
from rest_framework.views import APIView, Response
from .serializers import *


# Create your views here.
class UserView(APIView):

    def get(self, request, pk=None):
        if pk:
            user_profile = UserProfile.objects.get(pk=pk)
            ser = UserProfileSerializer(user_profile)
            return Response({"data": ser.data}, status=200)
        else:
            user_profile = UserProfile.objects.filter(user=request.user)
            ser = UserProfileSerializer(user_profile, many=True)
            return Response({"data": ser.data}, status=200)

    def post(self, request):
        data = request.data
