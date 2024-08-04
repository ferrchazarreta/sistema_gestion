from django.contrib import admin
from noticias.models import News,Category
from django.utils.html import format_html

# Register your models here.

@admin.register(News)
class NoticiasAdmin(admin.ModelAdmin):
    search_fields = ('title', 'created_at', 'category')
    list_filter = ('created_at','category')
    #exclude = ('price',)
    empty_value_display = "No hay datos para este campo"

    list_display = (
      'title',
      'short_description',
      'long_description',
      'created_at',
      'category',
      'image',

    )

    fieldsets = [
    ]

@admin.register(Category)
class NoticiasAdmin(admin.ModelAdmin):
    empty_value_display = "No hay datos para este campo"
    list_display = (
      'name',
    )
    fieldsets = []