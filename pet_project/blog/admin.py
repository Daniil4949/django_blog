from django.contrib import admin
from .models import *

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'category')
    list_filter = ('title', )

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )
    list_filter = ('name',)

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)


# Register your models here.
