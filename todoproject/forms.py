from django import forms

from .models import TodoList , TodoItems

class TodoListForm(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = ['description', ]



class TodoItemForm(forms.ModelForm):

    class Meta:
        model = TodoItems
        fields = ['todolist' , 'completed' , 'title']