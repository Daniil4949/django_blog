from django.contrib import admin
from .models import *


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'category', 'time_created')
    list_filter = ('time_created', 'title', )
    prepopulated_fields = {"slug": ('title', )}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )
    list_filter = ('name',)
    prepopulated_fields = {"slug": ('name', )}

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)
    list_filter = ('biography', )


class PhotoPostAdmin(admin.ModelAdmin):
    list_display = ('post', 'image')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'content', 'time_created')


admin.site.register(Comment, CommentAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(PhotoPost, PhotoPostAdmin)


# Register your models here.
