from django.shortcuts import render ,redirect
from django.views import generic
from django.urls import reverse_lazy

from .models import TodoItems , TodoList
from .forms import TodoItemForm , TodoListForm
from django.forms import inlineformset_factory

# Create your views here.


def home_todolist(request):
    todolistitems = TodoItems.objects.select_related('todolist').all()
    TodoListFormSet = inlineformset_factory(TodoList , TodoItems , fields = ('todolist',) , extra=1)

    if request.method == 'POST':
        formset = TodoListFormSet(request.POST , instance = todolistitems)
        if formset.is_valid():
            formset.save()

            return redirect('todolist_home')


    formset = TodoListFormSet()


    return render(request , 'todoproject/todo.html' , context={'formset':formset , 'todolist': todolistitems})



class UpdateToDOItem(generic.UpdateView):
    model = TodoItems
    fields = ['title' ,'completed'  , 'todolist']
    template_name = 'todoproject/update_todoitem.html'



class DeleteToDoItem(generic.DeleteView):
    model = TodoItems
    template_name = 'todoproject/delete_todoitemlist.html'
    success_url = reverse_lazy('todolist_home')