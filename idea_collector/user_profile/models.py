from django.db import models
from django.contrib.auth.models import User
from django.apps import apps

Position = apps.get_model('project_info', 'Position')
Function = apps.get_model('project_info', 'Function')


def generate_user_photo_path(instance, filename):
    return f'user_photo/{instance.user.pk}/{filename}'


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to=generate_user_photo_path, blank=True, null=True)
    position = models.ForeignKey(Position, on_delete=models.SET_NULL)
    functions = models.ManyToManyField(Function, related_name='user_competences')
    about = models.TextField(blank=True, null=True, default='')






