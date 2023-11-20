from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)
    icon = models.FileField(upload_to='category/')

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='user/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class PurchasedCourses(models.Model):
    course = models.ForeignKey('courses.Course', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.course.name


class UserOrders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey('courses.Course', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.name


class Saved(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.name


class SavedCourses(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey('courses.Course', on_delete=models.CASCADE)
    category = models.ForeignKey(Saved, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.name


class SavedBooks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey('library.Book', on_delete=models.CASCADE)
    category = models.ForeignKey(Saved, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.name


class UserSettings(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birth_date = models.DateTimeField()
    call_num = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.name
