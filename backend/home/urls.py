from rest_framework.routers import DefaultRouter
from .views import (
    BannerViewSet,
    VisionMissionViewSet,
    StatisticViewSet,
    InitiativeViewSet,
)

router = DefaultRouter()

router.register('banners', BannerViewSet, basename='banner')
router.register('vision-mission', VisionMissionViewSet, basename='vision-mission')
router.register('statistics', StatisticViewSet, basename='statistic')
router.register('initiatives', InitiativeViewSet, basename='initiative')

urlpatterns = router.urls