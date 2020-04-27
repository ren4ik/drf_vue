from rest_framework import serializers
from chat.models import Room, Chat
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ("id", "username")


class RoomSerializers(serializers.ModelSerializer):
	creater = UserSerializer()
	invited = UserSerializer(many=True)

	class Meta:
		model = Room
		fields = ("id", "creater", "invited", "date")


class ChatSerializers(serializers.ModelSerializer):
	"""Serializer chat GET"""
	user = UserSerializer()

	class Meta:
		model = Chat
		fields = ("user", "text", "date")


class ChatPostSerializers(serializers.ModelSerializer):
	"""Serializer chat POST"""
	class Meta:
		model = Chat
		fields = ("text", "room")

