from rest_framework import serializers
from account.models import User
from django.utils.encoding import smart_str, force_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from account.utils import Util

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password_confirm = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['id', 'email', 'full_name', 'password', 'password_confirm']
        # extra_kwargs = {
        #     'password': {'write_only': True},
        # }

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

class SendPasswordResetEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)
    class Meta:
        fields = ['email']

    def validate(self, attrs):
        email = attrs.get('email')
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email = email)
            uid = urlsafe_base64_encode(force_bytes(user.id))
            print('Encoded UID', uid)
            token = PasswordResetTokenGenerator().make_token(user)
            print('Password Reset Token', token)
            link = 'http://localhost:8000/api/reset-password/'+uid+'/'+token
            print('Password Reset Link', link)
            # Send Email
            body = 'Click the following link to reset your password '+link
            data = {
                'subject':'Reset Your Password',
                'body':body,
                'to':user.email
                }
            Util.send_email(data)
            return attrs
        else:
            raise serializers.ValidationError('You are not a Registered User')

class UserPasswordResetSerializer(serializers.Serializer):
  password = serializers.CharField(max_length=255, style={'input_type':'password'}, write_only=True)
  password_confirm = serializers.CharField(max_length=255, style={'input_type':'password'}, write_only=True)
  class Meta:
    fields = ['password', 'password_confirm']

  def validate(self, attrs):
    try:
      password = attrs.get('password')
      password_confirm = attrs.get('password_confirm')
      uid = self.context.get('uid')
      token = self.context.get('token')
      if password != password_confirm:
        raise serializers.ValidationError("Password and Confirm Password doesn't match")
      id = smart_str(urlsafe_base64_decode(uid))
      user = User.objects.get(id=id)
      if not PasswordResetTokenGenerator().check_token(user, token):
        raise serializers.ValidationError('Token is not Valid or Expired')
      user.set_password(password)
      user.save()
      return attrs
    except DjangoUnicodeDecodeError as identifier:
      PasswordResetTokenGenerator().check_token(user, token)
      raise serializers.ValidationError('Token is not Valid or Expired')