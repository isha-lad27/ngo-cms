from rest_framework import viewsets
from .models import Banner, VisionMission, Statistic, Initiative
from .serializers import (
    BannerSerializer,
    VisionMissionSerializer,
    StatisticSerializer,
    InitiativeSerializer,
)


class BannerViewSet(viewsets.ModelViewSet):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer


class VisionMissionViewSet(viewsets.ModelViewSet):
    queryset = VisionMission.objects.all()
    serializer_class = VisionMissionSerializer


class StatisticViewSet(viewsets.ModelViewSet):
    queryset = Statistic.objects.all()
    serializer_class = StatisticSerializer


class InitiativeViewSet(viewsets.ModelViewSet):
    queryset = Initiative.objects.all()
    serializer_class = InitiativeSerializer