from django.contrib import admin
from .models import Meetups,Location

class MeetupAdmin(admin.ModelAdmin):
    list_display=('title','slug')
    list_filter=('title','location',)
    prepopulated_fields={'slug':('title',)}


# Register your models here.

admin.site.register(Meetups,MeetupAdmin)
admin.site.register(Location)
