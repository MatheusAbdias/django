from clientes.views import ClientesViewSet
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
router.register("clientes", ClientesViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]
