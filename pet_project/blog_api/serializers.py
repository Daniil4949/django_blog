from email.policy import default
from rest_framework import serializers
from blog.models import Post, Category
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


class BlogSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault)

    class Meta:
        model = Post
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault)

    class Meta:
        model = Category
        fields = '__all__'
        

