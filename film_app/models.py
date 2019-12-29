from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.name}'


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.name} '


class Film(models.Model):
    title = models.CharField(max_length=30)
    release_date = models.DateField(default=timezone.now)
    cover_image = models.ImageField(upload_to='film_cover/', null=True)
    description = models.TextField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} '


class Director(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name}'


class Comments(models.Model):
    RATING_RANGE = (
        (1, 'Poor'),
        (2, 'Average'),
        (3, 'Good'),
        (4, 'Very Good'),
        (5, 'Excellent')
        )
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    rating = models.IntegerField(choices=RATING_RANGE, default=1)

    def __str__(self):
        return self.content

