from django.shortcuts import render
from rest_framework import viewsets,status
from rest_framework import generics
from django.contrib.auth.models import User
from .models import Vedio,Rating 
from .serializers import VedioSerializer,UserSerializer
from rest_framework.response import  Response
 	
class VideoViewSet(viewsets.ModelViewSet):
		queryset = Vedio.objects.all()
		serializer_class = VedioSerializer


# Serializers define the API representation.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
