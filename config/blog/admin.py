from django.contrib import admin
from .models import Article, Category, IPAddress

# Register your models here.

def make_published(modeladmin, request, queryset):
    queryset.update(status='p')
make_published.short_description = "Mark selected stories as published"


def make_draft(modeladmin, request, queryset):
    queryset.update(status='d')
make_draft.short_description = "Mark selected stories as draft"



class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'thumbnail_tag', 'slug', 'author', 'category_to_str', 'publish', 'is_special', 'status')
    list_filter = ('publish', 'status')
    ordering = ['-publish', '-status']
    search_fields = ['title', 'description']
    prepopulated_fields = {"slug": ("title",)}
    actions = [make_published, make_draft]

admin.site.register(Article, ArticleAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('position', 'title', 'slug', 'status')
    list_filter = (['status'])
    search_fields = ['title', 'slug']
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(IPAddress)