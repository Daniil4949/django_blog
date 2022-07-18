from email.policy import default
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
import uuid


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.CharField(max_length=100000000, blank=True, null=True,default="data:image/png;base64,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")
    time_created = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=1000,db_index=True, verbose_name='URL',null=True, blank=True, unique=True)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)    

    class Meta:
        ordering = ['-time_created']

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})


    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=1000, db_index=True, null=True, blank=True, verbose_name='URL', unique=True)

    def get_absolute_url(self):
        return reverse('posts_category', kwargs={'category_slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)    

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.SET_NULL)
    biography = models.TextField(blank=True, null=True)
    photo = models.ImageField(blank=True, upload_to=f"profile/", null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

class PhotoPost(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    image = models.TextField()

    def __str__(self):
        return self.post.title



# Create your models here.
