from django.shortcuts import render
from django.http import HttpResponse
from .models import Meetups

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


  # meetupsinmain=[
     # {
         #"title":"A first Meetups",
        # "location":"new york",
        # "slug":"a-first-meetups"
        # },

     # {
         #"title": "A second meetups",
        # "location":"paris",
         #"slug":"a-second-meetupos"
         #}
  # ]


   meetupsinmain=Meetups.objects.all()

   

   return render(request,'meetups/index.html',{
      "show_meetups":True,
      "meetups":meetups,
      "meetupinmain":meetupsinmain
   })



def meetup_details(request,meetup_slug):

#remember because its will return one object  not array to use selected_meetups['title or description] no no we will get  it as object property not array index
   selected_meetup=Meetups.objects.get(slug=meetup_slug)  # its like where slug=meetup_slug


   return render(request,"meetups/meetups-details.html",{
      
      "meetup_title":selected_meetup.title,
      "meetup_description":selected_meetup.description,
       "location":selected_meetup.location
      }
      )
