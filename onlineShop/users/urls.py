from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import RegistrUserView



router = DefaultRouter()
router.register('registr', RegistrUserView , basename='registration')


urlpatterns = [
    path('', include(router.urls)),
]