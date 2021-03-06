from django.db import models
from datetime import datetime


# Create your models here.

class News(models.Model):
    NewsId = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=100)
    URL = models.URLField(max_length=1000, default='www.cbc.ca')
    ReadFrequency = models.IntegerField()
    Created_Date = models.DateField(auto_created=True, default=datetime.now)

    def __str__(self):
        return self.Title


class NewsTag(models.Model):
    NewsTagId = models.AutoField(primary_key=True)
    TagName = models.CharField(max_length=100)
    TagFrequency = models.IntegerField()

    class Meta:
        ordering = ['-TagFrequency']

    def __str__(self):
        return self.TagName
