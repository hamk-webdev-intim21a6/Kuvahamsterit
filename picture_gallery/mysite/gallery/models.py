from django.db import models
from django.contrib.auth.models import User

#class User(models.User):



class Post(models.Model):
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    mod_date = models.DateTimeField('date modified', auto_now=True)
    omistaja = models.CharField(max_length=30)
    #author = models.ForeignKey(User, on_delete=models.CASCADE)