from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import  login_required



from .forms import UpdateUserForm, UpdateProfileForm
from .models import Profile
from accounts.models import User

# Create your views here.


@login_required()
def  profile(request):
    if request.user.is_customer:
        return render(request , 'profile/profile_user.html')

    elif request.user.is_admin:
        return render(request , 'profile/profile_admin.html')
