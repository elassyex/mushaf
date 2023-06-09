# Generated by Django 4.1.7 on 2023-03-13 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0018_alter_movie_category_alter_serie_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='category',
            field=models.CharField(choices=[('drama', 'دراما'), ('action', 'اكشن'), ('comedy', 'كوميدي'), ('romance', 'رومانسي'), ('war', 'حربي'), ('exciting', 'تشويق'), ('horror', 'رعب'), ('fantasia', 'خيال علمي'), ('deco', 'وثائقي'), ('real', 'واقعي')], max_length=100),
        ),
        migrations.AlterField(
            model_name='serie',
            name='category',
            field=models.CharField(choices=[('drama', 'دراما'), ('action', 'اكشن'), ('comedy', 'كوميدي'), ('romance', 'رومانسي'), ('war', 'حربي'), ('exciting', 'تشويق'), ('horror', 'رعب'), ('fantasia', 'خيال علمي'), ('deco', 'وثائقي'), ('real', 'واقعي')], max_length=100),
        ),
    ]
