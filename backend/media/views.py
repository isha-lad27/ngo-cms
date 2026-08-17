from django.shortcuts import render
from django.http import JsonResponse
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


def media_api(request):
    images = ImageGallery.objects.all()
    media_coverages = MediaCoverage.objects.all()

    image_data = [
        {
            "description": image.description,
            "image": request.build_absolute_uri(image.image.url),
        }
        for image in images
    ]

    coverage_data = [
        {
            "title": coverage.title,
            "url": coverage.url,
        }
        for coverage in media_coverages
    ]

    return JsonResponse({
        "images": image_data,
        "media_coverages": coverage_data,
    })