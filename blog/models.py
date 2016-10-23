'''
from __future__ import unicode_literals

from django.db import models
'''
from django.db import models
from django.utils import timezone


# Create your models here.
class Post(models.Model):
    '''
    This is a Post model with author,title,text,created_date,published_date,
    '''
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        '''
        This method publishes the post now
        '''
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
