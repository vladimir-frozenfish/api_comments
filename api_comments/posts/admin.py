from django.contrib import admin

from .models import Comment, Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'pub_date', 'author')
    search_fields = ('text',)
    list_filter = ('pub_date',)
    list_display_links = ('pk', 'text')
    empty_value_display = '-пусто-'


class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'created', 'author', 'post', 'parent')


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)


