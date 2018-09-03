from django.contrib import admin
from core.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner',
                    'is_published', 'published_at')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ("title",)}


admin.site.register(Post, PostAdmin)
