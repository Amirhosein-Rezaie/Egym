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


# serializer for orders and order_detials
class UserOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = ['username', 'first_name', 'last_name']


class OrderSeriliazer(serializers.ModelSerializer):
    user = UserOrderSerializer(read_only=True)

    class Meta:
        model = models.Order
        fields = '__all__'

# add or create order serializer
class AddOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Order
        fields = '__all__'