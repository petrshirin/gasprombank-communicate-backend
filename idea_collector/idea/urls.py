from django.urls import path, include
from .views import *

urlpatterns = [
        path('card/', IdeaView.as_view(), name='technology'),
        path('card/<int:pk>', IdeaView.as_view(), name='technology'),
    ]