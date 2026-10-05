from rest_framework import serializers
from . models import Student

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'

# for Student model
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model =Student
        fields = '__all__'