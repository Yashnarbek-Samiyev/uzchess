from django.db import models

# Create your models here.


class Main(models.Model):
    course = models.ForeignKey('courses.Course', on_delete=models.CASCADE)
    library = models.ForeignKey('library.Book', on_delete=models.CASCADE)
    live_video = models.URLField(blank=True, null=True)
    news = models.ForeignKey('news.News', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Languages(models.Model):
    name = models.CharField(max_length=255)
    icon = models.FileField(upload_to='language/')

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='country/')

    def __str__(self):
        return self.name


class Player1(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='player/')
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    language = models.ForeignKey(Languages, on_delete=models.CASCADE)
    result = models.CharField(max_length=255)
    all_rusult = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Player2(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='player/')
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    language = models.ForeignKey(Languages, on_delete=models.CASCADE)
    result = models.CharField(max_length=255)
    all_rusult = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Reyting(models.Model):
    player1 = models.ForeignKey(Player1, on_delete=models.CASCADE)
    player2 = models.ForeignKey(Player2, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    language = models.ForeignKey(Languages, on_delete=models.CASCADE)
    result = models.CharField(max_length=255)
    all_rusult = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Plays(models.Model):
    player1 = models.ForeignKey(Player1, on_delete=models.CASCADE)
    player2 = models.ForeignKey(Player2, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    reyting = models.ForeignKey(Reyting, on_delete=models.CASCADE)
    language = models.ForeignKey(Languages, on_delete=models.CASCADE)
    result = models.CharField(max_length=255)
    all_rusumlt = models.CharField(max_length=255)
    updated_at = models.DateTimeField(auto_now=True)
    play_type = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Notice(models.Model):
    image = models.ImageField(upload_to='notice/')
    title = models.CharField(max_length=255)
    notice = models.TextField()
