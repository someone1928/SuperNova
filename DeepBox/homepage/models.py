from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    caption=models.CharField(max_length=200)
    title=models.CharField(max_length=100)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user) +" "+ str(self.date.date())
    