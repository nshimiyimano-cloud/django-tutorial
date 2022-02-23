from tkinter.messagebox import RETRY
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
   #return HttpResponse("<h1>welcome page here</h1>")
   meetups=[
      {"title":"A first Meeting"},
      {"title": "A second meeting"}
   ]
   meetups=[
      {"title":"A first Meeting"},
      {"title": "A second meeting"}
   ]


   meetupsinmain=[
      {
         "title":"A first Meetups",
         "location":"new york",
         "slug":"a-first-meetups"
         },

      {
         "title": "A second meetups",
         "location":"paris",
         "slug":"a-second-meetupos"
         }
   ]
   

   return render(request,'meetups/index.html',{
      "show_meetups":True,
      "meetups":meetups,
      "meetupinmain":meetupsinmain
   })



   def meetup_details(request):
      selected_meetup={
         "title":"A First Meetup",
         "description":"This is the first meetup"
      }
      return render(request,"meetups/meetups-detail.html",{
         "meetup_title":selected_meetup['title'],
         "meetup_description":selected_meetup['description']

      })
