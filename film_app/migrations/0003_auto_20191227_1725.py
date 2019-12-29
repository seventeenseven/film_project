# Generated by Django 3.0.1 on 2019-12-27 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film_app', '0002_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='rating',
            field=models.IntegerField(choices=[(1, 'Poor'), (2, 'Average'), (3, 'Good'), (4, 'Very Good'), (5, 'Excellent')], default=1),
        ),
    ]