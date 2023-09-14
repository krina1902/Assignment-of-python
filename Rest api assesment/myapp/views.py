from django.shortcuts import render
from rest_framework import generics
from .models import Novel
from .serializers import NovelSerializer

# Create your views here.

class NovelList(generics.ListCreateAPIView):
	queryset=Novel.objects.all()
	serializer_class=NovelSerializer

class NovelDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset=Novel
	serializer_class=NovelSerializer
