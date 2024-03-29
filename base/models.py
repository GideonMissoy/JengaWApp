from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=211)
    description  = models.TextField(null=True, blank=True)
    status = models.BooleanField(default=False)
    