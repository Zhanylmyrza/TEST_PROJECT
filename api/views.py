from django.shortcuts import render
from rest_framework import viewsets
from .models import User, Product, Profile
from .serializers import UserSerializer, ProductSerializer, ProfileSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

def home(request):
    return render(request, 'index.html')