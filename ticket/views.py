from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import IntegrityError
from django.http import HttpResponse , HttpResponseRedirect
from django.contrib.auth import get_user_model
from django.views import generic
from django.db.models import Q

from .forms import CreateTicketForm, AssignTicketForm , AnswerTicketAdminForm


from .models import Ticket , AnswerAdmin


User = get_user_model()

def create_ticket(request):
    if request.method == 'POST':
        form = CreateTicketForm(request.POST)
        if form.is_valid():
            var1 = form.save(commit=False)
            var1.customer = request.user
            var1.save()
            messages.success(request, 'Your ticket has been submitted , admin will reach it soon ')
            return redirect('customer_active_tickets')
        else:
            messages.warning(request, 'Somthing went wrong , please check form errors')
            return redirect('create_ticket')

    else:
        form = CreateTicketForm()
        context = {'form': form}


    return render(request, 'ticket/create_ticket.html', context)


def customer_active_ticket(request):
    tickets = Ticket.objects.filter(customer=request.user , is_resolved=False)
    context = {'tickets': tickets}
    return render(request, 'ticket/customer_active_tickets.html', context)



# def customer_resolved_ticket(request):
#     tickets = Ticket.objects.filter(customer = request.user , is_resolved=True)
#     context = {'tickets':tickets}
#     return render(request , 'ticket/customer_resolved_tickets.html' , context)




def assign_ticket(request, ticket_id):
    ticket = Ticket.objects.get(id =ticket_id)
    if request.method == 'POST':
        form = AssignTicketForm(request.POST, instance=ticket)
        if form.is_valid():
            var1 = form.save(commit=False)
            var1.is_assigned_to_admin = True
            var1.save()
            messages.success(request, f'Ticket has been asigned to {var1.admin}')
            return redirect('customer_active_tickets')

        else:
            messages.warning(request, 'somthing went wrong , please check your input')
            return redirect('assign_ticket')

    else:
        form = AssignTicketForm(instance=ticket , )
        context = {'form': form , 'ticket':ticket}
        form.fields['admin'].queryset = User.objects.filter(is_admin = True)
        return render(request, 'ticket/assign_ticket.html', context)



def detail_tickets(request, ticket_id):
    ticket = Ticket.objects.get(id =ticket_id)
    context = {'ticket': ticket}
    return render(request, 'ticket/detail_ticket.html', context)



def tickets_admin(request):
    tickets = Ticket.objects.filter(is_assigned_to_admin = True ).order_by('-choice_user_neccesiry')
    return render(request , 'ticket/tickets_admin.html' , context={'tickets':tickets})




def answer_ticket_admin(request , ticket_id):
    ticket = Ticket.objects.get(id = ticket_id)
    users = User.objects.filter(is_customer = True)
    if request.method == 'POST':
        form = AnswerTicketAdminForm(request.POST  , instance = ticket)
        if form.is_valid():
                ticket.is_resolved = True
                form.save()
                return redirect('tickets_admin')

    else:
         form = AnswerTicketAdminForm(instance=ticket)


    return render(request , 'ticket/answer_admin.html' , context = {'form':form , 'ticket' : ticket})



def search_result_tickets(request):
    tickets = Ticket.objects.all()
    return render(request , 'ticket/tickets_search_page.html' , context={'tickets':tickets})



class SearchResultsTicket(generic.ListView):
    model = Ticket
    context_object_name = "tickets"
    template_name = "ticket/tickets_search_page.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        return Ticket.objects.filter(
            Q(ticket_id__icontains = query)
        )