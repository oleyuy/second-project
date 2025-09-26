from django.db import models
from django.utils.html import format_html
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.models import Group, Permission
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
    
# this model defines the new user profile
class MyUserManager(BaseUserManager):
    def create_user(self,email,name,birth_year,password=None,**extra_fields):
        if not email: raise ValueError('email doesnt exist')
        email = self.normalize_email(email)
        user = self.model(name=name, email=email, birth_year=birth_year, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    def create_superuser(self,email,name,birth_year,password=None,**extra_fields):
      extra_fields.setdefault('is_staff',True)
      extra_fields.setdefault('is_superuser', True) 
      if extra_fields.get('is_staff') is not True:
          raise ValueError ('must be is istaff true')
      if extra_fields.get('is_superuser') is not True:
          raise ValueError ('must be is superuser true')
 
      return self.create_user(email, name, birth_year, password, **extra_fields)
    def get_by_natural_key(self, email):
        return self.get(email=email)

class MyUser(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=15)
    email = models.EmailField(max_length=255, unique=True)
    birth_year = models.IntegerField()
    date_joined = models.DateTimeField(auto_now_add=True)

    #allowings
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'birth_year']
    objects = MyUserManager()

    # дописать менеджер
    def __str__(self):
        return self.email