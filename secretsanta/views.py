from django.http import HttpResponseRedirect
from django.urls import reverse 
from django.shortcuts import render, redirect
from django.views import generic, View
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.models import User, Group
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import NewUserForm
from .models import Participants
from . import pairs_generator


def index(request):

    if (request.user.is_authenticated):
        if (Participants.objects.filter(giver = request.user).exists() or Participants.objects.filter(receiver = request.user).exists()):
            try:
                field = "receiver"
                current_user = request.user
                p_giver = current_user
                temp = Participants.objects.get(giver = current_user)
                p_receiver = getattr(temp, field)
            except:
                field = "giver"
                current_user = request.user
                p_giver = current_user
                temp = Participants.objects.get(receiver = current_user)
                p_receiver = getattr(temp, field)

        else:
            current_user = User.objects.get(id = request.user.id)
            p_giver = None
            p_receiver = None
    else:
        current_user = request.user
        p_giver = None
        p_receiver = None

    context={'current_user': current_user, 'p_giver': p_giver, 'p_receiver': p_receiver,}  
    return render(request, 'index.html',context=context)

class UserListView(LoginRequiredMixin, generic.ListView):
    model = User

    def get_queryset(self):
        return User.objects.exclude(is_superuser = True)

class ParticipantsListView(LoginRequiredMixin, generic.ListView):
    model = Participants

def match_pairs(request):
    participants = User.objects.all().exclude(is_superuser=True)
    participants_names = [p.id for p in participants]
    i = 0
    Givers = []
    Receivers = []
    if request.method == "POST":
        [temp_givers, temp_receivers] = pairs_generator.generate_match(participants_names)
        while i < len(temp_givers):
            if temp_givers[i] == None:
                Givers.append(None) 
            else:
                Givers.append(User.objects.get(pk = temp_givers[i]))
            Receivers.append(User.objects.get(pk = temp_receivers[i]))
            Participants.objects.create(giver = Givers[i], receiver = Receivers[i])
            i += 1
        messages.success(request, "Matching successful! Here's the list.")
        return redirect('participants')
    else:
        messages.error(request, "Woops. Something went wrong. Please try again.")
        return redirect('participants')

def participants_reset(request):
    if request.method == "POST":
        Participants.objects.all().delete()
        messages.success(request, "Old Santa's list has been deleted successfully.") 
        return redirect('delete-completed')
    else:
        messages.error(request, "Woops. Something went wrong. Please try again.")
        return redirect('participants')

def register_administrator(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            administrators = Group.objects.get(name='Administrators') 
            administrators.user_set.add(user)
            user.is_staff = True
            user.save()
            messages.success(request, "New Administrator added successfully." )
            return redirect("index")
        messages.error(request, "Information you entered is inconsistent. Please try again.")
    form = NewUserForm()
    return render (request, "secretsanta/register.html", context={"register_form":form})

def register_employee(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            employees = Group.objects.get(name='Employees') 
            employees.user_set.add(user)
            user.save()
            messages.success(request, "New Employee added successfully" )
            return redirect("index")
        messages.error(request, "Information you entered is inconsistent. Please try again.")
    form = NewUserForm()
    return render (request, "secretsanta/register.html", context={"register_form":form})