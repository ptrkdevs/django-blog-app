from django.db import models
from uuid import uuid4
import datetime

# Create your models here.
class Post(models.Model):

    id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid4)
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.created)
