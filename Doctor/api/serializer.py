from rest_framework import serializers
from .models import Contact,Subscribe,Blog

class ContactSerializer(serializers.ModelSerializer):

    class Meta:

        model = Contact
        fields = ('firstname','lastname','email','phone','message')


class AddBlogSerializer(serializers.ModelSerializer):

    class Meta:

        model = Blog
        fields = ('title', 'image', 'content', 'tag', 'description')

class SubscribeSerializer(serializers.ModelSerializer):

    email = serializers.EmailField()

    class Meta:
        model = Subscribe
        fields = ("email",)