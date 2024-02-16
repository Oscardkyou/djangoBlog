from rest_framework import serializers
from .models import Post, Author

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'text', 'author', 'created_date']

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['user', 'bio']


