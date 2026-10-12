from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UniversityViewSet, CampusViewSet

router = DefaultRouter()
router.register(r'universities', UniversityViewSet, basename='university')
router.register(r'campuses', CampusViewSet, basename='campus')

urlpatterns = [
    path('', include(router.urls)),
]