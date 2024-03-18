from django.contrib import admin
from . import models

# Register your models here.

class CommentInline(admin.TabularInline):
    model = models.Comment

class PosttAdmin(admin.ModelAdmin):
    inlines = [CommentInline, ]
    list_display = ("title", "author",)
    
class PostInline(admin.TabularInline):
    model = models.Post

class AuthorAdmin(admin.ModelAdmin):
    inlines = [PostInline, ]
    list_display = ("name", )


admin.site.register(models.Post,PosttAdmin)
admin.site.register(models.Author,AuthorAdmin)
admin.site.register(models.Comment)
