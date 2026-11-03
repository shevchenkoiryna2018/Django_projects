from django.contrib import admin
from .models import Post, Category, Tag, Profile, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'published_date', 'user', 'content_length']
    list_filter = ['category', 'published_date']
    search_fields = ['title', 'content']
    filter_horizontal = ['tags']
    ordering = ('-published_date',)
    list_per_page = 10

    @admin.display(description="Довжина тексту")
    def content_length(self, obj):
        return len(obj.content)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']
    ordering = ('name',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']
    ordering = ('name',)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user']
    search_fields = ['user_username']
    ordering = ('user',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'post', 'author', 'created_at', 'text_length']
    list_filter = ['created_at']
    search_fields = ['author__username', 'text', 'post__title']
    ordering = ('-created_at',)
    list_per_page = 10

    @admin.display(description="Довжина коментаря")
    def text_length(self, obj):
        return len(obj.text)

