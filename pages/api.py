from .models import User
from rest_framework import viewsets, permissions
from .serializers import UserSerializer, IntervaloTiempoSerializer
from .models import IntervaloTiempo
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class IntervaloTiempoViewSet(viewsets.ModelViewSet):
    serializer_class = IntervaloTiempoSerializer
    queryset = IntervaloTiempo.objects.all()