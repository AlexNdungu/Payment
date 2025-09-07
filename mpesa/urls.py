from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MpesaApiTest

router = DefaultRouter()
router.register("mpesa", MpesaApiTest, basename="mpesa")

urlpatterns = [
    path("", include(router.urls)),
]