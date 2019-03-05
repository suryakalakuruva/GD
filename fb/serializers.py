from rest_framework import serializers
from . import models


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'author', 'title', 'created_date', 'post_pics',)
        model = models.Post



class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'post', 'author', 'text', 'created_date',)
        model = models.Comment