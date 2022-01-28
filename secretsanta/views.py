from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from django.views import generic
from django.contrib.auth.models import User
from .forms import NewUserForm
# Create your views here.


def index(request):
   
    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits+1

    # Render the HTML template index.html with the data in the context variable.
    return render(request, 'index.html', context={'num_visits': num_visits},
    )

class UserListView(generic.ListView):
    model = User

def register_user(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("main:homepage")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render (request=request, template_name="secretsanta/register.html", context={"register_form":form})