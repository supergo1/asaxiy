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
    list_filter = [
        ('author', admin.RelatedOnlyFieldListFilter),
        ('genre', admin.RelatedOnlyFieldListFilter)
    ]


admin.site.register(Book, BookAdmin)


class BookOrderAdmin(admin.ModelAdmin):
    list_display = ('book', 'user', 'status')
    list_display_links = ('book', 'user', 'status')
    list_filter = [
        ('status', admin.ChoicesFieldListFilter),
        ('is_paid', admin.BooleanFieldListFilter),
        ('created_at', admin.DateFieldListFilter),
        ('user', admin.RelatedFieldListFilter)
    ]


admin.site.register(BookOrder, BookOrderAdmin)
