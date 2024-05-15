from django import forms

from django.contrib.auth.models import User

from .models import Profile , InformationCart


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email']



class UpdateProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file' , 'placeholder':"" }))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    class Meta:
        model = Profile
        fields = [ 'avatar', 'bio' , 'first_name' , 'last_name' , 'phone_number' , 'national_code']
        error_messages = {
            'avatar': {
                'required': ("")
            },

            'bio': {
                'required': ("")
            },
        }


class UpdateInformationCartForm(forms.ModelForm):

    class Meta:
        model = InformationCart
        fields = ['number_cart' , 'cvv2' , 'number_shabaa_cart' , 'number_account_cart']



