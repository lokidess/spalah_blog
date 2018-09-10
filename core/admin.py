from django.contrib import admin
from core.models import Post, Tags, Image


def make_published(modeladmin, request, queryset):
    queryset.update(is_published=True)


def make_unpublished(modeladmin, request, queryset):
    queryset.update(is_published=False)


class ImageInline(admin.TabularInline):
    model = Image
    extra = 0


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'full_name', 'is_published')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ("title",)}
    actions = (make_published, make_unpublished)
    list_filter = ['tags', 'owner']
    inlines = [ImageInline]
    # filter_horizontal = ['tags']
    # def has_add_permission(self, request):
    #     return False
    #
    # def has_change_permission(self, request, obj=None):
    #     return False
    #
    # def has_delete_permission(self, request, obj=None):
    #     return False

    def full_name(self, obj):
        return f"<a target='_blank' href='/admin/auth/user/{obj.owner.id}/'>{obj.owner.first_name} {obj.owner.last_name}</a>"

    full_name.short_description = 'Name'
    full_name.allow_tags = True
    full_name.admin_order_field = 'owner'


class TagsAdmin(admin.ModelAdmin):
    list_display = ('name', )
    list_editable = ('name', )
    list_display_links = None


admin.site.register(Post, PostAdmin)
admin.site.register(Tags, TagsAdmin)
admin.site.register(Image)
