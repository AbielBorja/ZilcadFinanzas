from django.contrib import admin
from .models import Role, User, BaseGeneral, IntervaloTiempo 

# Register your models here.
admin.site.register(Role)
admin.site.register(User)
admin.site.register(BaseGeneral)
admin.site.register(IntervaloTiempo)