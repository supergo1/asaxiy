from rest_framework import serializers
from account.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name', 'last_name')


class BalanceAPIView(serializers.ModelSerializer):
    user = UserSerializer

    class Meta:
        model = Balance
        fields = ('id', 'balance', 'ball')