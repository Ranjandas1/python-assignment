from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WheelFormViewSet

router = DefaultRouter()
router.register(r'form/wheelform', WheelFormViewSet)


urlpatterns = [
    path('', include(router.urls)),
]

      