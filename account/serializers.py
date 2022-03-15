from rest_framework import serializers
from account.models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['email', 'full_name', 'password', 'password_confirm']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    # validate password and password_confirm
    def validate(self, attrs):
        if attrs.get('password') != attrs.get('password_confirm'):
            raise serializers.ValidationError('Passwords do not match')
        return super().validate(attrs)
    
    # create user
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    class Meta:
        model = User
        fields = ['email', 'password']

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'full_name']

class UserChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=255, min_length=8, style={'input_type':'password'}, write_only=True)
    password_confirm = serializers.CharField(max_length=255, min_length=8, style={'input_type':'password'}, write_only=True)
    old_password = serializers.CharField(style={'input_type':'password'}, write_only=True)
    class Meta:
        model = User
        fields = ['old_password', 'password', 'password_confirm']

    # validate password and password_confirm
    def validate(self, attrs):
        password = attrs.get('password')
        password_confirm = attrs.get('password_confirm')
        user = self.context.get('user')
        if password != password_confirm:
            raise serializers.ValidationError("Password and Confirm Password doesn't match")
        user.set_password(password)
        user.save()
        return attrs
    
    # validate old_password
    def validate_old_password(self, value):
        user = self.context.get('user')
        if not user.check_password(value):
            raise serializers.ValidationError('Old password is incorrect')
        return value
        