from rest_framework import serializers
from . import models


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'user', 'image', 'cover', 'worked', 'studied', 'company', 'lives', 'Home', 'created_date',)
        model = models.Profile


