
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.



class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    post_pics = models.FileField(upload_to = 'post_pics', blank=True)
    

    

    def __str__(self):
        return self.title




class Comment(models.Model):
    post = models.ForeignKey('fb.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    # approved_comment = models.BooleanField(default=False)
    # comment_pic = models.ImageField(upload_to = 'comment_pic',blank=True,null=True)

    # def approve(self):
    #     self.approved_comment = True
    #     self.save()

    def __str__(self):
        return self.text



class Friend(models.Model):
    users = models.ManyToManyField(User)
    current_user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='owner',null=True )

    @classmethod
    def make_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(current_user=current_user)

        friend.users.add(new_friend)


    @classmethod
    def lose_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(current_user=current_user)

        friend.users.remove(new_friend)