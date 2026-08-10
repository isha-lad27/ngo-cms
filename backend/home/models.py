from django.db import models


class Banner(models.Model):
    image_url = models.URLField(max_length=255)
    title = models.CharField(max_length=150)
    description = models.TextField()
    order = models.IntegerField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class VisionMission(models.Model):
    vision_title = models.CharField(max_length=150)
    vision_description = models.CharField(max_length=200)
    mission_title = models.CharField(max_length=150)
    mission_description = models.CharField(max_length=200)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.vision_title


class Statistic(models.Model):
    label = models.CharField(max_length=100)
    value = models.CharField(max_length=50)
    order = models.CharField(max_length=150)
    status = models.CharField(max_length=50, default="Active")

    def __str__(self):
        return self.label


class Initiative(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    image_url = models.URLField(max_length=150)
    order = models.IntegerField()
    status = models.TextField(default="Active")

    def __str__(self):
        return self.title