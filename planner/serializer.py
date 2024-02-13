from rest_framework import serializers
from taggit.serializers import (TagListSerializerField, TaggitSerializer)
from .models import User, Post, Trip, Comment

class UserSerializer(serializers.ModelSerializer):
    photo = serializers.ImageField()
    about = serializers.StringRelatedField()
    date_joined = serializers.DateTimeField(format="%I:%M %p, %a %d %B %Y")

    class Meta:
        model = User
        fields = ['id', 'username', 'about', 'first_name', 'last_name', 'email', 'date_joined', 'photo']

class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    title = serializers.StringRelatedField()
    body = serializers.StringRelatedField()
    location = serializers.StringRelatedField()
    photo =  photo = serializers.ImageField()
    timestamp = serializers.DateTimeField(format="%I:%M %p, %a %d %B %Y")
    likes = serializers.StringRelatedField(many=True)
    tags = TagListSerializerField()

    class Meta:
        model = Post
        fields = '__all__'
        #fields = ['author', 'title', 'body', 'location', 'photo', 'timestamp', 'likes']

class TripSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField()
    destination = serializers.StringRelatedField()
    departure =  serializers.DateField(format="%a %d %B %Y")
    arrival =  serializers.DateField(format="%a %d %B %Y")

    class Meta:
        model = Trip
        fields = ['owner', 'destination', 'departure', 'arrival']

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    post = serializers.StringRelatedField()
    content = serializers.StringRelatedField()
    parent = serializers.StringRelatedField()
    timestamp = serializers.DateTimeField(format="%I:%M %p, %a %d %B %Y")

    class Metal:
        model = Comment
        fields = ['user', 'post', 'content', 'parent', 'timestamp']
