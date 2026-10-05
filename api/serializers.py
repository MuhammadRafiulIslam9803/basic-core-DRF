from rest_framework import serializers
from . models import Student
from django.contrib.auth.models import User

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'

# for Student model
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model =Student
        fields = '__all__'

class RegistrationSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=100, write_only=True)

    def validate(self, data):
       if User.objects.filter(username=data['username']).exists():
           raise serializers.ValidationError("Username already exists")
       if User.objects.filter(email=data['email']).exists():
           raise serializers.ValidationError("Email already exists")
       return data
   
    def create(self, validated_data):
       user = User(
           username=validated_data['username'],
           email=validated_data['email']
       )
       user.set_password(validated_data['password'])
       user.save()
       return user

# for Login

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()  