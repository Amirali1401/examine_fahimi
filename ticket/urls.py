from django.urls import path

from . import views

urlpatterns = [
    path('create_ticket/' , views.create_ticket , name = 'create_ticket'),
    path('customer_active_tickets/' , views.customer_active_ticket , name = 'customer_active_tickets'),
    path('assign_ticket/<int:ticket_id>/' , views.assign_ticket , name = 'assign_ticket'),
    path('ticket_details/<int:ticket_id>/' , views.detail_tickets , name = 'detail_ticket'),
    path('tickets_admin/' , views.tickets_admin , name = 'tickets_admin'),
    path('answer_admin/<int:ticket_id>/' , views.answer_ticket_admin , name='answer_admin'),
    path('search_tickets/' , views.search_result_tickets , name = 'search_tickets'),
    path('is_resolved_tickets/' , views.is_resolved_tickets , name = 'is_resolved_tickets'),
    path('description_answer/<int:ticket_id>/' , views.description_answer_tickets , name = 'description_answer'),

    path('search_result/' , views.SearchResultsTicket.as_view() , name='search_result'),
]