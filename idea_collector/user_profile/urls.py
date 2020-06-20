from django.urls import path, include
from .views import *

urlpatterns = [
    path('', UserView.as_view(), name='my_info'),
    path('<int:pk>', UserView.as_view(), name='user'),

]