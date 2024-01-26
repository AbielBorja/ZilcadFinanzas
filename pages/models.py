from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Permission, Group

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('El campo Email es obligatorio')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

class Role(models.Model):
    ROLE_CHOICES = (
        ('admin', 'Administrador'),
        ('editor', 'Editor'),
        ('viewer', 'Visualizador'),
    )

    name = models.CharField(max_length=10, choices=ROLE_CHOICES, unique=True)

    def __str__(self):
        return self.get_name_display()

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    user_created = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(null=True, blank=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)


    # Agregar related_name único para evitar conflictos
    groups = models.ManyToManyField(Group, related_name='pages_user_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='pages_user_permissions')

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return self.email

class BaseGeneral(models.Model):  # Convención Camel Case para el nombre del modelo
    tipo = models.CharField(max_length=150)
    folio = models.CharField(max_length=150)
    fecha_de_atencion = models.DateTimeField(auto_now=False, auto_now_add=False)
    cliente = models.CharField(max_length=150)
    sitio = models.CharField(max_length=150)
    site_id_telmex = models.IntegerField(unique=False, null=False, blank=False)
    ciudad = models.CharField(max_length=150)
    estado = models.CharField(max_length=150)
    proveedor_IDC = models.CharField(max_length=150)
    coordinador_IDC = models.CharField(max_length=150)
    hora_llegada_a_sitio = models.TimeField(auto_now=False, auto_now_add=False)
    hora_de_ingreso_a_sucursal = models.TimeField(auto_now=False, auto_now_add=False)
    hora_frente_equipo = models.TimeField(auto_now=False, auto_now_add=False)
    hora_de_salida = models.TimeField(auto_now=False, auto_now_add=False)
    tiempo_en_sitio = models.TimeField(auto_now=False, auto_now_add=False)
    status = models.CharField(max_length=150)  # Agregado valor predeterminado
    costo_servicio = models.FloatField(blank=False, null=False)
    costo_recoleccion = models.FloatField(blank=False, null=False)
    retiro = models.FloatField(blank=True, null=False)
    viaticos = models.FloatField(blank=True, null=False)
    costo_herramienta = models.FloatField(blank=True, null=False)
    total = models.FloatField(blank=False, null=False)
    servicio_pagado = models.FloatField(blank=True, null=False)
    viatico_pagado = models.FloatField(blank=True, null=False)
    recoleccion_pagada = models.FloatField(blank=True, null=False)
    herramienta = models.FloatField(blank=True, null=False)
    total_pagado = models.FloatField(blank=True, null=False)
    penalizacion = models.FloatField(blank=True, null=False)
    observaciones = models.CharField(max_length=150)
    cuenta_por_pagar = models.FloatField(blank=False, null=False)


class IntervaloTiempo(models.Model):
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    costo_servicio = models.DecimalField(max_digits=10, decimal_places=2)