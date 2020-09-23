from django.contrib import admin
from posts.models import Post, Like, Comment

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    model = Post


class LikeAdmin(admin.ModelAdmin):
    model = Like


class CommentAdmin(admin.ModelAdmin):
    model = Comment


admin.site.register(Post, PostAdmin)
admin.site.register(Like, LikeAdmin)
admin.site.register(Comment, CommentAdmin)
