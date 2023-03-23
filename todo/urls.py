from django.urls import path

from todo.views import todo_list, category_list

urlpatterns = [
    path('todo-list/', todo_list),
    path('categories/', category_list),
]