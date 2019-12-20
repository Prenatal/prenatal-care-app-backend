from rest_framework import serializers
# from django.contrib.auth.hashers import check_password
from django.db.models import Q
from .models import User
import re


class UserRegistrationSerializer(serializers.ModelSerializer):
    """Serializers registration requests and creates a new user."""

    # Ensure passwords are at least 8 characters long, no longer than 128
    # characters, and can not be read by the client.
    password = serializers.CharField(
        write_only=True
    )
    email = serializers.EmailField()
    username = serializers.CharField()

    class Meta:
        model = User
        # List all of the fields that could possibly be included in a request
        # or response, including fields specified explicitly above.
        fields = '__all__'

    def validate_password(self, value):
        if not re.search(r'[0-9]', value):
            raise serializers.ValidationError(
                "Weak password. Include atleast one integer")
        elif value.isupper() or value.islower():
            raise serializers.ValidationError(
                "Password should contain both upper and lower cases")
        elif value.isdigit():
            raise serializers.ValidationError(
                "Password can not contain only integers")
        return value

    def validate_email(self, value):
        user_email_db = User.objects.filter(email=value)
        if user_email_db.exists():
            raise serializers.ValidationError("Email already in use")
        return value

    def validate_username(self, value):
        username_db = User.objects.filter(username=value)
        if username_db.exists():
            raise serializers.ValidationError("Username already exists")
        elif len(value) <= 2 or len(value) > 25:
            raise serializers.ValidationError(
                "Username should longer than two characters")
        elif re.compile('[!@#$%^&*:;?><.0-9]').match(value):
            raise serializers.ValidationError("Invalid characters not allowed")
        return value

    def create(self, validated_data):
        # Use the `create_user` method we wrote earlier to create a new user.
        return User.objects.create_user(**validated_data)


class UserLoginSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=255, read_only=True)
    email = serializers.EmailField(allow_blank=True, required=False)
    username = serializers.CharField(allow_blank=True, required=False)

    class Meta:
        model = User
        fields = [
            'token',
            'username',
            'password',
            'email'
        ]
        extra_kwargs = {"password":
                        {"write_only": True}
                        }

    def validate(self, data):
        user_obj = None
        email = data.get("email", None)
        username = data.get("username", None)
        password = data.get("password")
        if not email and not username:
            raise serializers.ValidationError(
                "A username or email is required to login")

        if password is None:
            raise serializers.ValidationError(
                'A password is required to log in.'
            )

        user = User.objects.filter(
            Q(email=email) |
            Q(username=username)
        )
        if user.exists():
            user_obj = user.first()
        else:
            raise serializers.ValidationError(
                " This Email or Username doesn't exist")
        if user_obj:
            if not user_obj.check_password(password):
                raise serializers.ValidationError(
                    "Incorrect credentials please try again")
        return {
            'email': user_obj.email,
            'username': user_obj.username,
            'token': user_obj.token
        }
