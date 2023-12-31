# Generated by Django 3.2.9 on 2023-11-20 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0001_initial'),
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='country/')),
            ],
        ),
        migrations.CreateModel(
            name='Languages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('icon', models.FileField(upload_to='language/')),
            ],
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='notice/')),
                ('title', models.CharField(max_length=255)),
                ('notice', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Player1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='player/')),
                ('result', models.CharField(max_length=255)),
                ('all_rusult', models.CharField(max_length=255)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.country')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.languages')),
            ],
        ),
        migrations.CreateModel(
            name='Player2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='player/')),
                ('result', models.CharField(max_length=255)),
                ('all_rusult', models.CharField(max_length=255)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.country')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.languages')),
            ],
        ),
        migrations.CreateModel(
            name='Reyting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.CharField(max_length=255)),
                ('all_rusult', models.CharField(max_length=255)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.country')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.languages')),
                ('player1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.player1')),
                ('player2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.player2')),
            ],
        ),
        migrations.CreateModel(
            name='Plays',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.CharField(max_length=255)),
                ('all_rusumlt', models.CharField(max_length=255)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('play_type', models.CharField(max_length=255)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.country')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.languages')),
                ('player1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.player1')),
                ('player2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.player2')),
                ('reyting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.reyting')),
            ],
        ),
        migrations.CreateModel(
            name='Main',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('live_video', models.URLField(blank=True, null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course')),
                ('library', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.book')),
            ],
        ),
    ]
