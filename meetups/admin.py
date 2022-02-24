from django.contrib import admin
from .models import Meetups

class MeetupAdmin(admin.ModelAdmin):
    list_display=('title','slug')
    list_filter=('title',)


# Register your models here.

admin.site.register(Meetups,MeetupAdmin)
