from django.contrib import admin
from .models import Anime, Genre

# Register your models here.
class AnimeAdmin(admin.ModelAdmin):
    readonly_fields = ['image_preview']
    filter_horizontal = ('genres',)
    
admin.site.register(Anime, AnimeAdmin)
admin.site.site_header = "Anime Admin"
admin.site.register(Genre)