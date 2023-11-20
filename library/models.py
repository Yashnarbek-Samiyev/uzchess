from django.db import models


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    pages = models.IntegerField()
    about = models.TextField(blank=True)
    year = models.IntegerField()
    price = models.IntegerField()
    image = models.ImageField(
        upload_to='images/', default='images/None/No-img.jpg')
    rate = models.IntegerField(default=0)

    language = models.ForeignKey('main.Languages', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Orders(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.CharField(max_length=100)
    price = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
