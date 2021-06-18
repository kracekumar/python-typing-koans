from __future__ import annotations

from django.db import models
from django.db.models import Avg, Max, QuerySet, Count, Q, Manager


class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()


class Publisher(models.Model):
    name = models.CharField(max_length=300)


class BooksQuerySet(models.QuerySet):
    def get_small_books(self):
        return self.filter(pages__lte=100)

    def get_thick_books(self):
        return self.filter(pages__gte=500)


class Book(models.Model):
    name = models.CharField(max_length=300)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField()
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    pubdate = models.DateField()

    objects = Manager.from_queryset(BooksQuerySet)()


class Shelf(models.Model):
    name = models.CharField(max_length=200)


def create_books() -> None:
    murakami = Author.objects.create(name="Haruki Murakami", age=71)
    publisher = Publisher.objects.create(name="Harvill Secker")
    book = Book.objects.create(
        name="First Person Singular: Stories",
        pages=256,
        price="646.50",
        pub_date="2021-04-01",
    )
    book.authors.add(murakami)
    book.objects.archive()
    book.objects.unarchive()
    book.authors

    shelf = Shelf.objects.create(name="Classics")
    qs = Shelf.objects.get_queryset()
    qs.filter(name="Classics")


if __name__ == "__main__":
    create_books()
