from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default.jpg', upload_to ='profile_pics')
	cover = models.ImageField(default='default.jpg', upload_to ='cover_pics')
	worked = models.CharField(max_length=200,blank=True,null=True)
	studied = models.CharField(max_length=200,blank=True,null=True)
	company = models.CharField(max_length=200,blank=True,null=True)
	lives = models.CharField(max_length=200,blank=True,null=True)
	Home = models.CharField(max_length=200,blank=True,null=True)
	created_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.user.username
	
#Create your models here.

