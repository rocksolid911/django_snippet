from django.contrib import admin
from snippets.models import Snippet


@admin.register(Snippet)
class SnippetAdmin(admin.ModelAdmin):
    list_display = ['title', 'language', 'style', 'owner', 'created']
    list_filter = ['language', 'style', 'created']
    search_fields = ['title', 'code']

