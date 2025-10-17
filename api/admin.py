from django.contrib import admin
from .models import Driver, Team

# Inline per vedere i piloti direttamente dentro il Team
class DriverInline(admin.TabularInline):
    model = Driver
    extra = 0

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    inlines = [DriverInline]
    list_display = ('team_name', 'points')

@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ('number', 'full_name', 'team', 'points')
    list_filter = ('team',)
    search_fields = ('full_name', 'acronym')
