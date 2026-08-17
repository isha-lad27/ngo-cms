from django.contrib import admin
from .models import PressRelease, MediaCoverage, ImageGallery, Video


@admin.register(PressRelease)
class PressReleaseAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date', 'created_at')
    search_fields = ('title', 'description')
    list_filter = ('release_date',)


@admin.register(MediaCoverage)
class MediaCoverageAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'created_at')
    search_fields = ('title', 'url')


@admin.register(ImageGallery)
class ImageGalleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'uploaded_at')
    search_fields = ('description',)
    list_filter = ('uploaded_at',)


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'video_url', 'description', 'uploaded_at')
    search_fields = ('video_url', 'description')
    list_filter = ('uploaded_at',)