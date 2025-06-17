from rest_framework import serializers

from .models import User, UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source = "user.username",read_only=True)
    class Meta:
        model = UserProfile
        fields = [
            'username',
            'first_name',
            'last_name',
            'bio',
            'phone_number',
            'country',
            'city',
            'role',
        ]

    # Validate all Fields
    def validate_first_name(self, value):
        if any(char.isdigit() for char in value):
            raise serializers.ValidationError("First name cannot contain digits.")
        if not value[0].isupper():
            raise serializers.ValidationError("First name should start with a capital letter.")
        return value

    def validate_last_name(self, value):
        if any(char.isdigit() for char in value):
            raise serializers.ValidationError("Last name cannot contain digits.")
        if not value[0].isupper():
            raise serializers.ValidationError("Last name should start with a capital letter.")
        return value

    def validate_phone_number(self, value):
        if not value.isdigit():
            raise serializers.ValidationError("Phone number should contain only digits.")
        if len(value) != 10:
            raise serializers.ValidationError("Phone number must be exactly 10 digits.")
        return value

    def validate_country(self, value):
        blocked_countries = ['north korea', 'turkey']
        if value.lower() in blocked_countries:
            raise serializers.ValidationError(f"{value} is not an allowed country.")
        if any(char.isdigit() for char in value):
            raise serializers.ValidationError("Country name cannot contain digits.")
        return value

    def validate_city(self, value):
        if any(char.isdigit() for char in value):
            raise serializers.ValidationError("City name cannot contain digits.")
        return value

    def validate_bio(self, value):
        if len(value.strip()) < 10:
            raise serializers.ValidationError("Bio must be at least 10 characters long.")
        return value

    def validate_role(self, value):
        allowed_roles = ['admin', 'moderator', 'user', 'guest']
        if value.lower() not in allowed_roles:
            raise serializers.ValidationError(f"Role must be one of: {', '.join(allowed_roles)}.")
        return value
class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer()

    class Meta:
        model = User
        fields  = [
            'username',
            'email',
            'password',
            'profile'
            ]
        # password field used in POST and PUT, its not apear in GET, LIST, RETRIEVE
        extra_kwargs = {
            'password':{"write_only":True},
        }
        
    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        password = validated_data.pop("password")

        user = User.objects.create(**validated_data)
        user.set_password(password) # encrypt the password before saving it
        user.save()
        UserProfile.objects.create(user=user,**profile_data) # create the profile for the user
        return user
    
    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        password = validated_data.pop("password")

        if password:
            instance.set_password(password)
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.save()

        if profile_data:
            profile = instance.profile
            for attr , value in profile_data.items():
                setattr(profile , attr , value)
            profile.save()
            
        return instance
    