from django.contrib import admin

from .models import Product, Comment


class CommentInLine(admin.TabularInline):
    model = Comment
    fields = ['user', 'text', 'demonstrable', 'satisfaction', ]
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'availability', 'datetime_modified', ]

    inlines = [
        CommentInLine,
    ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['product', 'user', 'text', 'demonstrable', 'satisfaction', 'datetime_modified', ]
