from django.db import models
from django.utils.html import format_html

# Create your models here.
class Anime(models.Model):
    title = models.CharField(max_length=75)
    description = models.TextField()
    year = models.IntegerField(choices=[(year, year) for year in range(1900, 2100)], default=2023)
    genres = models.ManyToManyField('Genre', related_name='animes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='anime_images/')

    def image_preview(self):
        if self.image:
            return  format_html(
            '<img src="{}" style="width: 100px; height: auto;" />',
            self.image.url
            )
        return "No image"

    image_preview.short_description = "Preview"

    def __str__(self):
        return self.title
    
class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name