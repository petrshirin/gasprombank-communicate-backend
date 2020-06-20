from django.urls import path, include
from .views import *

urlpatterns = [
    path('technology/', TechnologyView.as_view(), name='technology'),
    path('block/', BlockView.as_view(), name='block'),
    path('function/', FunctionView.as_view(), name='function'),
    path('department/', DepartmentView.as_view(), name='department'),
    path('position/', PositionView.as_view(), name='position'),
]