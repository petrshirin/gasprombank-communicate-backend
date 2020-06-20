from django.db import models
from django.apps import apps

# models from user profile
Function = apps.get_model('project_info', 'Function')
Department = apps.get_model('project_info', 'Department')
Technology = apps.get_model('project_info', 'Technology')
Block = apps.get_model('project_info', 'Block')


# Create your models here.
class Idea(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    block = models.ForeignKey(Block, on_delete=models.CASCADE)
    departments = models.ManyToManyField(Department, related_name='idea_departments')
    technologies = models.ManyToManyField(Technology, related_name='idea_technologies')
    functions = models.ManyToManyField(Function, related_name='idea_function')



