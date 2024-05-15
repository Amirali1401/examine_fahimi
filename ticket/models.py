from django.db import models
from django.conf import settings

import random
import string

# Create your models here.

def generic_unique_code():
    code_length = 6
    characters = string.ascii_letters + string.digits

    while(True):
        code = ''.join(random.choice(characters) for _ in range(code_length))
        if not Ticket.objects.filter(ticket_id = code ).exists():
            return code


class Ticket(models.Model):

    CHOICES_NECCESIRY = (
        (1, "فوری"),
        (2, "غیر فوری"),
    )


    customer = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete  = models.CASCADE )
    admin = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete = models.DO_NOTHING , related_name="admin" , null=True , blank = True)
    ticket_id = models.CharField(max_length= 10 , unique=True , default = generic_unique_code)
    ticket_title = models.CharField(max_length=50)
    ticket_description  = models.TextField()
    status = models.CharField(max_length=20 , choices=(('Active' , 'Active') , ('Pending','Pending') , ('Resolved' , 'Resolved')) , default='Pending')
    created_at = models.DateTimeField(auto_now_add = True)
    last_modified = models.DateTimeField(auto_now=True)
    is_resolved = models.BooleanField(default=False)
    contact_mode = models.CharField(max_length=20 , choices = (('Phone' , 'Phone') , ('Email' , 'Email')))
    is_assigned_to_admin = models.BooleanField(default = False)
    resolution_steps = models.TextField(null = True , blank = True)
    choice_user_neccesiry = models.CharField(max_length=20,  choices=((  'فوری' , 1 ) , ( 'غیرضروری' , 2 )) , default=2)


    def __str__(self):
        return f'{self.ticket_title}'




class AnswerAdmin(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete = models.CASCADE)
    content = models.TextField()
    ticket = models.ForeignKey(Ticket , on_delete = models.CASCADE)




