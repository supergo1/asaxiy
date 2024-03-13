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
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)
    if user is not None:
        access_token = create_access_token(user.id)
        refresh_token = create_refresh_token(user.id)
        return Response({'access_token': access_token, 'refresh_token': refresh_token})
    else:
        return Response({'error': 'Invalid credentials'})


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
    last_name = requset.data.get("last_name")
    age = request.data.get('age')
    phone = request.data.get('phone')
    username = request.data.get('username')
    password = request.data.get('password')
    usercreate = User.objects.create_user(
        first_name=first_name,
        last_name=last_name,
        age=age,
        phone=phone,
        username=username,
        password=password
    )
    return Response(serializer, status=200)


