from django.db import models

# Create your models here.

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Status(models.TextChoices):
    DRAFT = 'DF', 'Draft'
    PUBLISHED = 'PB', 'Published'

class PublishedManager(models.Manager):
 def get_queryset(self):
    return super().get_queryset()\
        .filter(status=Post.Status.PUBLISHED)

class Post(models.Model):

    META_ROBOTS_CHOICES = (
        ('index', 'Index'),
        ('noindex', 'Noindex'),
    )

    META_FOLLOW_CHOICES = (
        ('follow', 'Follow'),
        ('nofollow', 'Nofollow'),
    )
    
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2,
            choices=Status.choices,
            default=Status.DRAFT)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')

    objects = models.Manager() # The default manager.
    published = PublishedManager() # Our custom manager.
    
    meta_title = models.CharField(max_length=255, null=True, blank=True)
    meta_description = models.TextField(null=True, blank=True)
    robots = models.CharField(max_length=10, choices=META_ROBOTS_CHOICES, null=True, blank=True)
    follow = models.CharField(max_length=10, choices=META_FOLLOW_CHOICES, null=True, blank=True)
    canonical_url = models.URLField(null=True, blank=True)
    schema = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['-publish']

    indexes = [
        models.Index(fields=['-publish']),
    ]
    def __str__(self):
        return self.title