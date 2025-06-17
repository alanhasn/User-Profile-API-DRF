from rest_framework import serializers

from .models import User, UserProfile


class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields  = ['username']

class UserProfileSerializer(serializers.ModelSerializer):
    user = Userserializer(read_only=True)

    class Meta:
        model = UserProfile
        fields = [
            'user',
            'first_name',
            'last_name',
            'bio',
            'phone_number',
            'country',
            'city',
            'role',
        ]