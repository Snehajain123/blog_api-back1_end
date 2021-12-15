from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Post, Comment
from datetime import datetime


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password','email')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = self.validated_data('password')
        user.set_password(password)
        user.save()
        return user

class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    comments = serializers.StringRelatedField(many=True)
    no_of_comments = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'owner', 'comments', 'no_of_comments']

    def get_no_of_comments(self, object):
        return object.comments.count()

    
class UserSerializer(serializers.ModelSerializer):
    posts = serializers.StringRelatedField(many=True, read_only=True)
    no_of_posts = serializers.SerializerMethodField()
    comments = serializers.StringRelatedField(many=True, read_only=True)
    no_of_comments = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'posts', 'no_of_posts', 'comments', 'no_of_comments']
    
    def get_no_of_posts(self, object):
        return object.posts.count()

    def get_no_of_comments(self, object):
        return object.comments.count()

class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Comment
        fields = ['id', 'comment', 'owner', 'post']
