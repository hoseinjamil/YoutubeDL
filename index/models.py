from django.db import models


class Video(models.Model):
    title = models.CharField(max_length=500)
    video_id = models.CharField(max_length=20, unique=True)
    url = models.URLField()