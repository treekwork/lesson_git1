from django.contrib import admin

from todo.models import ToDo, Category


@admin.register(ToDo)
class ToDoAdmin(admin.ModelAdmin):
    list_display = ('title', 'deadline')
    list_filter = ('category', )
    search_fields = ('title', 'desc')

admin.site.register(Category)
