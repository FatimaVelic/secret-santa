from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.urls import reverse 
from django.contrib import messages
from django.views import generic, View
from django.contrib.auth.models import User
from .forms import NewUserForm
from .models import Participants
from . import pairs_generator
# Create your views here.


def index(request):
   
    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits+1
    context={'num_visits': num_visits}  

    # Render the HTML template index.html with the data in the context variable.
    return render(request, 'index.html',context=context)

class UserListView(generic.ListView):
    model = User

class ParticipantsListView(generic.ListView):
    model = Participants

def matchPairs(request):
    participants = User.objects.all().exclude(is_superuser=True)
    participants_names = [p.id for p in participants]
    i = 0
    Givers = []
    Receivers = []
    if request.method == "POST":
        [givers, receivers] = pairs_generator.generate_match(participants_names)
        while i < len(receivers):
            if givers[i] == None:
                Givers.append(None) 
            else:
                Givers.append(User.objects.filter(pk = givers[i]))
            Receivers.append(User.objects.filter(pk = receivers[i]))
            
            Participants.objects.create(giver = Givers[i], receiver = Receivers[i])
            messages.success(request, "Matching successful! Here's the list.")
            return redirect('participants')
    else:
        messages.error(request, "Woops. Something went wrong. Please try again.")
        return redirect('participants')


"""class MatchPairs(View):
    template_unmatched = "match_pairs_new.html"
    template_matched = "match_pairs_completed.html"
     
    def get(self, request):
        is_paired = matching_mechanism.is_paired()
        participants = User.objects.all()
        context = {
            ['is_paired'] = is_paired,
            ['user_list'] = participants
        }
        template = self.template_matched if (
            is_paired) else self.template_unmatched
        return render(request=request, template_name=template, context=context)

    def post(self, request):
        participants = User.objects.count()
        if participants < 3:
            mes = ('`There has to be at least three people for this to work.')
            messages.add_message(self.request, messages.ERROR, mes)
            return redirect(reverse('match-pairs'))
        if not matching_mechanism.is_paired():
            matching_mechanism.make_pairs()
        participants = User.objects.all()
        context = {
            ['user_list'] = participants
        }
        return render(request=request, template_name=self.template_matched, context=context)
"""
    
def register_user(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("index")
        messages.error(request, "Woops. Something went wrong. Please try again.")
    form = NewUserForm()
    return render (request, "secretsanta/register.html", context={"register_form":form})