# Generated by Django 3.2.9 on 2023-11-20 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rules',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('twitter_url', models.URLField()),
                ('facebook_url', models.URLField()),
                ('instagram_url', models.URLField()),
                ('youtube_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='news')),
                ('description', models.TextField()),
                ('watching', models.BooleanField(default=False)),
                ('twitter_url', models.URLField()),
                ('facebook_url', models.URLField()),
                ('instagram_url', models.URLField()),
                ('youtube_url', models.URLField()),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.languages')),
            ],
        ),
    ]
