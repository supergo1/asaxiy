from django.urls import path
from .views import *

urlpatterns = [
    path('login/', login, name='login'),
    path('signin/', signin, name='signin'),
    path('user-create/', user_create, name='user-create')
]




