from django.shortcuts import render
from rest_framework.decorators import  api_view
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from .serializers import *
from django.contrib.auth import  authenticate
# from .jwt_auth import create_access_token, decode_access_token, create_refresh_token, decode_refresh_token
from rest_framework.authtoken.models import Token
from .models import *


@api_view(['POST'])
def signin(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        token = Token.objects.get_or_create(user=user)[0]
        return Response({'token': token.key})
    else:
        return Response('Invalid credentials')


@api_view(['POST'])
def user_create(request):
    first_name = request.data.get('first_name')
    last_name = request.data.get("last_name")
    phone = request.data.get('phone')
    username = request.data.get('username')
    password = request.data.get('password')
    user = User.objects.create_user(
        first_name=first_name,
        last_name=last_name,
        phone=phone,
        username=username,
        password=password
    )
    token = Token.objects.get_or_create(user=user)
    print(request)
    return Response({'ok': True, 'token': token[0].key}, status=200)


