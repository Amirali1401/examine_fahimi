from django.db import models

# Create your models here.




class TodoList(models.Model):
	description = models.TextField()



class TodoItems(models.Model):
	todolist = models.ForeignKey(TodoList , on_delete=models.CASCADE)
	title = models.CharField(max_length = 30)
	completed = models.CharField(max_length=20 , default = 'Imcompleted'  , choices = (('Finished' , 'Finished') , ('Imcompleted' , 'Imcompleted')) )

