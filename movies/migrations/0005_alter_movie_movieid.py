# Generated by Django 4.1.7 on 2023-03-04 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_alter_movie_movieid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='movieid',
            field=models.CharField(max_length=265, primary_key=True, serialize=False, unique=True),
        ),
    ]
