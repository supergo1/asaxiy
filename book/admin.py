from django.contrib import admin
from .models import *


admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Tag)


class BookAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            'Asosiy ',
            {
                "fields": ['title', 'price'],
            },
        ),
        (
            "Advanced options",
            {
                "classes": ["collapse"],
                "fields": ['author', 'genre', 'tag'],
            },
        ),
    ]
    list_display = ('title', 'author', 'price')
    search_fields = ('title',)
    list_display_links = ('title', 'price')


admin.site.register(Book, BookAdmin)
