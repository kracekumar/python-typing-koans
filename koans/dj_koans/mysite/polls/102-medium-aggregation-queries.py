from django.db import models
from django.db.models import Avg, Max, QuerySet, Count, Q
import typing as t
from django.db.models import Case, Value, When


class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

class Publisher(models.Model):
    name = models.CharField(max_length=300)

    @classmethod
    # Annotate the return type
    # Note: you may need to create a new type
    def count_by_publisher(cls):
        return Publisher.objects.annotate(num_books=Count('book'))

class Book(models.Model):
    name = models.CharField(max_length=300)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField()
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    pubdate = models.DateField()

    @classmethod
    # Annotate the return type
    def get_avg_price(cls):
        return Book.objects.all().aggregate(Avg('price'))


class Store(models.Model):
    name = models.CharField(max_length=300)
    books = models.ManyToManyField(Book)


def print_publishers_count() -> None:
    pub_count = Publisher.count_by_publisher()
    for pub in pub_count:
        print(pub.name, pub.num_books)


def create_russian_authors_filter():
    return Q(name__isubstring='tolstoy') | Q(name__isubstring='turganev') | Q(name__isubstring='fyodor') | Q(name__isubstring='chekov')


def create_french_authors_filter():
    return Q(name__isubstring='balzac') | Q(name__isubstring='camus') | Q(name__isubstring='sartre') | Q(name__isubstring='flaubert')

# Annotate the return value
def get_author_avg_ratings():
    ret = Author.objects.annotate(average_rating=Avg('book__rating')).values('name', 'average_rating')
    return ret


def get_author_countries():
    russian_authors = create_russian_authors_filter()
    french_authors = create_french_authors_filter()
    when_russian = When(russian_authors, then=Value('russia'))
    when_french = When(russian_authors, then=Value('french'))
    case = Case(when_russian, when_french, default=Value('others'))
    ret = Author.objects.annotate(country=case).values_list('name', 'country')
    return ret
