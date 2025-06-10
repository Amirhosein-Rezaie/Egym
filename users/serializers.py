from rest_framework import serializers
from . import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        exclude = ['password']


# the serializer of the register new user
class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = '__all__'

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = models.CustomUser(**validated_data)
        user.set_password(password)
        user.save()
        return user


# serializers of exercise
class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Exercise
        fields = '__all__' 