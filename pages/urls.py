from django.urls import path, include
from rest_framework import routers
from . import views
from . import controler
from .api import UserViewSet, IntervaloTiempoViewSet

router = routers.DefaultRouter()
router.register(r'/user', UserViewSet, basename='user')
router.register(r'/intervalo-tiempo-list', IntervaloTiempoViewSet, basename='intervalo_tiempo_list')


urlpatterns = [
    # URL VIEWS
    path('finanzas', views.finanzas, name='cargar_datos'),
    path('charts', views.charts, name="charts"),
    path('login', views.login, name="login"),
    path('password', views.password, name="password"),
    path('register', views.register, name="register"),
    path('tables', views.tables, name="tables"),
    path("layout-static", views.layout, name="layout"),
    path("layout-sidenav-light", views.light, name="light"),
    path("401", views.error_401, name="error_401"),
    path("404", views.error_404, name="error_404"),
    path("500", views.error_500, name="error_500"),

    # Agrega otras URL para eliminar si es necesario
    path('api', include(router.urls)),

    path('', views.index, name='index'),

    # URL API DATA - CONTROLER
    path('api/dataTableFinanzas', controler.dataTableFinanzas, name="dataTableFinanzas"),
]