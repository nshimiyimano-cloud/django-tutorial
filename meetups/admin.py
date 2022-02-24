from django.contrib import admin
from .models import Meetups,Location,Participant

class MeetupAdmin(admin.ModelAdmin):
    list_display=('title','date','location')
    list_filter=('title','date',)
    prepopulated_fields={'slug':('title',)}


# Register your models here.

admin.site.register(Meetups,MeetupAdmin)
admin.site.register(Location)
admin.site.register(Participant)
