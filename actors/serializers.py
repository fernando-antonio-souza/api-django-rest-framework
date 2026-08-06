from rest_framework import serializers
from actors.models import Actor


class ActorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fiels = "__all__"