from django.db import models
from main.models import Languages


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return self.name


class Filter(models.Model):
    choose_rate = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    languages = models.ForeignKey('main.Languages', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='courses')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    languages = models.ForeignKey('main.Languages', on_delete=models.CASCADE)
    filter = models.ForeignKey(Filter, on_delete=models.CASCADE)
    rate = models.IntegerField()
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class Comments(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    comment = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Certificate(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='certificates')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Report(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
