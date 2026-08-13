from django.contrib import admin
from .models import OurStory, CoreValue, Program, TeamMember


@admin.register(OurStory)
class OurStoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'updated_at')


@admin.register(CoreValue)
class CoreValueAdmin(admin.ModelAdmin):
    list_display = ('id', 'value', 'created_at', 'updated_at')


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'role', 'created_at', 'updated_at')