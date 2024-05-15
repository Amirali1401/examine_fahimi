from django import forms

from .models import Ticket , AnswerAdmin

class CreateTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = [ 'ticket_title' , 'ticket_description' , 'contact_mode' , 'choice_user_neccesiry']



class AssignTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['admin' , ]



class AnswerTicketAdminForm(forms.ModelForm):
    class Meta:
        model = AnswerAdmin
        fields = [ 'content' ]

