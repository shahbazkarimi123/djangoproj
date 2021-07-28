from django.db import models
from django.contrib.auth.models import User
from datetime import time,datetime

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=264)
    # publish_date = models.DateTimeField(time)
    body = models.TextField(max_length=500)
    url = models.TextField(max_length=300)
    image = models.ImageField(upload_to = 'images/')
    icon = models.ImageField(upload_to = 'images/',default='default.png',blank=True)
    votes_total = models.IntegerField(default=1)
    time = models.TimeField(auto_now=True,null=False)
    hunter = models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[ :100]
    
    def mytime(self):
        return self.time
        
    
    