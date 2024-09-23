from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField(null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    nationality = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name


class BaseWork(models.Model):
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    publication_date = models.DateField(null=True, blank=True)

    class Meta:
        abstract = True  # This is an abstract base class

    def __str__(self):
        return self.title


class Book(BaseWork):
    pages = models.PositiveIntegerField()
    volume = models.CharField(max_length=50, null=True, blank=True)
    chapters = models.PositiveIntegerField()


class Movie(BaseWork):
    runtime = models.DurationField()
    awards = models.TextField(null=True, blank=True)
    rating = models.DecimalField(max_digits=3, decimal_places=1)


class Music(BaseWork):
    duration = models.DurationField()
    album = models.CharField(max_length=100, null=True, blank=True)
    tracks = models.PositiveIntegerField(null=True, blank=True)

