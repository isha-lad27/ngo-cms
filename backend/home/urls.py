from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    BannerViewSet,
    VisionMissionViewSet,
    StatisticViewSet,
    InitiativeViewSet,
)


router = DefaultRouter()

router.register(r'banners', BannerViewSet)
router.register(r'vision-mission', VisionMissionViewSet)
router.register(r'statistics', StatisticViewSet)
router.register(r'initiatives', InitiativeViewSet)


urlpatterns = [
    path('', include(router.urls)),
]