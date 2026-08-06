from django.contrib import admin
from .models import *

admin.site.site_header = "NGO CMS Administration"
admin.site.site_title = "NGO CMS"
admin.site.index_title = "Welcome to NGO Management System"


@admin.register(Admin)
class AdminAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "phone")
    search_fields = ("full_name", "email")
    ordering = ("full_name",)


@admin.register(Donor)
class DonorAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "phone", "donation_amount")
    search_fields = ("full_name", "email")
    ordering = ("full_name",)


@admin.register(Beneficiary)
class BeneficiaryAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'age', 'gender', 'address')
    search_fields = ('full_name', 'gender')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("project_name", "budget", "start_date", "end_date")
    search_fields = ("project_name",)
    list_filter = ("start_date",)


@admin.register(Volunteer)
class VolunteerAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "phone", "skills")
    search_fields = ("full_name", "skills")


@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ("donor_name", "amount", "purpose", "donation_date")
    search_fields = ("donor_name", "purpose")
    list_filter = ("donation_date",)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("event_name", "location", "event_date")
    search_fields = ("event_name", "location")
    list_filter = ("event_date",)

from .models import Contact

admin.site.register(Contact)