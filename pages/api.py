from .models import User
from rest_framework import viewsets, permissions
from .serializers import UserSerializer, IntervaloTiempoSerializer
from .models import IntervaloTiempo
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer

class IntervaloTiempoViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = IntervaloTiempoSerializer

    def get_queryset(self):
        return IntervaloTiempo.objects.filter(usuario=self.request.user)