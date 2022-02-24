
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Meetups, Participant
from .forms import RegistrationForm

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
   
   try:

      if request.method == "GET":
         #remember because its will return one object  not array to use selected_meetups['title or description] no no we will get  it as object property not array index
         selected_meetup=Meetups.objects.get(slug=meetup_slug)  # its like where slug=meetup_slug
         registration_form=RegistrationForm()

          # print(selected_meetup.image.url) # will be like this /images/dress.jpg
         return render(request,"meetups/meetups-details.html",{
         "meetup_found":True,
          #"meetup_title":selected_meetup.title,  let we change by only get selected_mmetup object
          #"meetup_description":selected_meetup.description,
         "meetup":selected_meetup,
         "form":registration_form
         })

      else:
         registration_form=RegistrationForm(request.POST)   
         if registration_form.is_valid():
            selected_meetup=Meetups.objects.get(slug=meetup_slug) 
           # partticipant=registration_form.save()
            user_email=registration_form.cleaned_data['email'] # _ its like to say was_create this second param present/determine take status that alredy exist but first param or key its for to use when data there is not exist in database(just its data to be saved in database)
            partticipant, _= Participant.objects.get_or_create(email=user_email)
            selected_meetup.participant.add(partticipant) #because if we have selected_mmetup already we have participants here because we have this field in Meetups model in db
            return redirect("confirm-registration",meetup_slug=meetup_slug)



      return render(request,"meetups/meetups-details.html",{
         "meetup_found":True,
         "meetup":selected_meetup,
         "form":registration_form
         })   
           

      
   except Exception as exc:
       print(exc)
       return render(request,"meetups/meetups-details.html",{
          "meetup_found":False   

       })



def confirm_registration(request,meetup_slug):
   meetup= Meetups.objects.get(slug=meetup_slug)  # slug=..is slug field from database here is like where clouse in mysql where slug=meetup_slug
   return render(request,'meetups/registration-success.html',{      # we do this because succes page come for this function plays role there
      "organizer_email": meetup.organizer_email
   }) 

