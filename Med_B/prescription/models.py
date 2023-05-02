from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class Image(models.Model):
    caption = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images")
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)


    def __str__(self):
        return self.caption
    