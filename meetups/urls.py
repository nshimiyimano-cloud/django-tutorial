from django.urls import URLPattern, path


from django.urls import path
from . import views

urlpatterns=[
    path('meetups',views.index,name='meetups'),
    path('meetups/<slug:meetup_slug>/success',views.confirm_registration,name='confirm-registration'),
    path('meetups/<slug:meetup_slug>',views.meetup_details,name='meetup-detail')  
]