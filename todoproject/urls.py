from django.urls import path

from . import views

urlpatterns = [
    path('' , views.home_todolist , name = 'todolist_home'),
    path('<int:pk>/update_todoitem/' , views.UpdateToDOItem.as_view() , name='update_todoitem'),
    path('<int:pk>/delete_todoitem/' , views.DeleteToDoItem.as_view() , name='delete_todoitem'),

]