from rest_framework import serializers
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

    # The client should not be able to send a token along with a registration
    # request. Making `token` read-only handles that for us.

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
