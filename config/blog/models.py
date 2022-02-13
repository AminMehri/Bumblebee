from ipaddress import ip_address
from pyexpat import model
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import related
from django.urls import reverse
from django.utils import timezone
from django.utils.html import format_html
from account.models import User
from django.contrib.contenttypes.fields import GenericRelation
from comment.models import Comment



class ArticleManager(models.Manager):
    def published(self):
        return self.filter(status='p')

# Create your models here.


class IPAddress(models.Model):
    ip_address = models.GenericIPAddressField()

    def __str__(self):
        return self.ip_address



class Category(models.Model):
    title = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128 ,unique=True)
    thumbnail = models.ImageField(upload_to="images")
    status = models.BooleanField(default=True)
    position = models.IntegerField()

    class Meta:
        ordering = ['position']


    def __str__(self):
        return self.title



class Article(models.Model):
    STATUS_CHOICES = (
        ('d', 'draft'),
        ('p', 'published'),
        ('i', 'investigation'),
        ('b', 'back'),
    )
    title = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128 ,unique=True)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to="images")
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name="articles")
    category = models.ManyToManyField(Category, related_name="articles")
    promote = models.BooleanField(default=False)
    is_special = models.BooleanField(default=False)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    comments = GenericRelation(Comment)
    hits = models.ManyToManyField(IPAddress, through="ArticleHit", blank=True, related_name="hits")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-publish']

    def category_published(self):
        return self.category.filter(status=True)

    def get_absolute_url(self):
        return reverse("account:home")

    def thumbnail_tag(self):
        return format_html("<img width=100 height=75 src='{}' >".format(self.thumbnail.url))

    def category_to_str(self):
        return ",".join([category.title for category in self.category_published()])
    category_to_str.short_description = 'category'


    objects = ArticleManager()

class ArticleHit(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    ip_address = models.ForeignKey(IPAddress, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

