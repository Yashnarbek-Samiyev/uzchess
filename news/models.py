from django.db import models

# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=50)
    updated_at = models.DateTimeField(auto_now_add=True)
    language = models.ForeignKey('main.Languages', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='news')
    description = models.TextField()
    watching = models.BooleanField(default=False)
    twitter_url = models.URLField()
    facebook_url = models.URLField()
    instagram_url = models.URLField()
    youtube_url = models.URLField()

    def __str__(self):
        return self.title


class Rules(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()

    twitter_url = models.URLField()
    facebook_url = models.URLField()
    instagram_url = models.URLField()
    youtube_url = models.URLField()

    def __str__(self):
        return self.title
