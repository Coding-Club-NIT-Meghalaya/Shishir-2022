from django.contrib import admin
from .models import Gallery, Notification, Year, Event, TeamMember

# Register your models here.


@admin.register(Year)
class YearAdmin(admin.ModelAdmin):
    list_display = ['festival_name','year', 'start_date', 'end_date']


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['name', 'start_date', 'end_date',
                    'type', 'duration', 'year', 'total_prize', 'description', 'registration_link', 'image', 'doc_link', 'live_link']


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ['member_name', 'type',
                    'email', 'image', 'event_name', 'contact_no']


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['event_name','image']


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ['notification']