from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save

from core.managers import PostManager


class Tags(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Post(models.Model):

    NEWS_TYPE = 0
    STORY_TYPE = 1
    ART_TYPE = 2

    TYPE_CHOICES = (
        (NEWS_TYPE, 'News'),
        (STORY_TYPE, 'Story'),
        (ART_TYPE, 'Art')
    )

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255,
                            help_text="URL like line",
                            verbose_name='URL like str')
    body = models.TextField()
    owner = models.ForeignKey(User)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(blank=True, null=True)
    file = models.FileField(upload_to="posts_files", blank=True, null=True)
    type = models.IntegerField(null=True, choices=TYPE_CHOICES)
    tags = models.ManyToManyField(Tags)

    objects = PostManager()

    def some_function(self):
        return "Test"

    def __str__(self):
        return self.title


def send_mail_on_new_post(**kwargs):
    if kwargs['created']:
        print('Email was sent!')


post_save.connect(send_mail_on_new_post, sender=Post)
