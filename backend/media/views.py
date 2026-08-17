from django.shortcuts import render
from .models import ImageGallery, MediaCoverage


def media_gallery(request):
    images = ImageGallery.objects.all()
    media_coverages = MediaCoverage.objects.all()

    return render(
        request,
        "media.html",
        {
            "images": images,
            "media_coverages": media_coverages,
        }
    )