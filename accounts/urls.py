from django.urls import path

from . import views

urlpatterns = [
    path('change_info/' , views.profile , name='change_account'),
    path('change_cart/' , views.change_cart_information_view , name ='change_cart'),

]