from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=128)
    intro = models.TextField()
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('blog:post-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title


class Image(models.Model):
    name = models.CharField(max_length=64, unique=True)
    slug = models.SlugField(max_length=64, unique=True, null=True)
    image = models.ImageField(upload_to='post_pics/%Y-%m-%d')
    date = models.DateTimeField(default=timezone.now)
    is_header = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('blog:image-detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name
