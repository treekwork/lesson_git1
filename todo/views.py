from django.shortcuts import render

from todo.models import ToDo, Category

def todo_list(request):
    todo_objects = ToDo.objects.all()
    return render(request, 'index.html', {'todo': todo_objects})

def category_list(request):
    cat_objects = Category.objects.all()
    return render(request, 'category.html', {'categories': cat_objects})
