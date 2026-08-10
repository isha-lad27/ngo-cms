from rest_framework import serializers

from .models import (
    Banner,
    VisionMission,
    Statistic,
    Initiative,
)


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'


class VisionMissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisionMission
        fields = '__all__'


class StatisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistic
        fields = '__all__'


class InitiativeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Initiative
        fields = '__all__'