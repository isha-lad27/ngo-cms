from django.contrib import admin
from .models import Banner, VisionMission, Statistic, Initiative


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'order', 'status')
    list_filter = ('status',)
    search_fields = ('title', 'description')
    ordering = ('order',)


@admin.register(VisionMission)
class VisionMissionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'vision_title',
        'mission_title',
        'last_updated'
    )
    search_fields = (
        'vision_title',
        'mission_title',
    )


@admin.register(Statistic)
class StatisticAdmin(admin.ModelAdmin):
    list_display = ('id', 'label', 'value', 'order', 'status')
    list_filter = ('status',)
    search_fields = ('label',)
    ordering = ('order',)


@admin.register(Initiative)
class InitiativeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'order', 'status')
    list_filter = ('status',)
    search_fields = ('title', 'description')
    ordering = ('order',)