from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from profile.forms import UpdateUserForm, UpdateProfileForm , UpdateInformationCartForm
from profile.models import Profile , InformationCart

# Create your views here.




@login_required
def profile(request):
    profile = Profile.objects.get(user_id = request.user)
    user_form = UpdateUserForm(instance=request.user)
    profile_form = UpdateProfileForm(instance = profile)

    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user )
        profile_form = UpdateProfileForm( request.POST ,  request.FILES , instance = profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='profile_user')

    return render(request, 'accounts/change_information.html', {'user_form': user_form , 'profile_form':profile_form , 'profile':profile})



@login_required()
def change_cart_information_view(request):
    cart = InformationCart.objects.get(user = request.user)
    form = UpdateInformationCartForm(instance = cart)

    if request.method == 'POST':
        form = UpdateInformationCartForm(data = request.POST , instance = cart)
        if form.is_valid():
            form.save()
            return redirect(to = 'profile_user')


    return render(request , 'accounts/change_information_cart.html' , context={'form':form})