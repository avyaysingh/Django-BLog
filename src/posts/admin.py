from django.contrib import admin
from .models import Author, Catagory, Post, Comment, PostView
# Register your models here.

admin.site.register(Author)
admin.site.register(Catagory)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(PostView)
