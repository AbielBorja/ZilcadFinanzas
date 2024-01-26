from rest_framework import serializers
from .models import Role, User, IntervaloTiempo

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('id', 'name')

class UserSerializer(serializers.ModelSerializer):
    role = RoleSerializer()  

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'role', 'user_created')
        read_only_fields = ('user_created', )

class IntervaloTiempoSerializer(serializers.ModelSerializer):
    class Meta:
        model = IntervaloTiempo
        fields = ['id', 'hora_inicio', 'hora_fin', 'costo_servicio']