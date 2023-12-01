from __future__ import annotations


import random
from django.db import models
from django.db.models import QuerySet


from books.constants import BOOK_SPINES_QUANTITY


class Book(models.Model):
    title = models.CharField(max_length=512)
    author_full_name = models.CharField(max_length=512)
    year_of_publishing = models.SmallIntegerField()
    copies_printed = models.IntegerField()
    short_description = models.TextField()

    def __str__(self) -> str:
        return f'{self.title} ({self.author_full_name})'

    @classmethod
    def fetch_books(cls) -> QuerySet[Book]:
        return cls.objects.order_by('id')

    @classmethod
    def find_book_by_id(cls, book_id: int) -> Book | None:
        try:
            return cls.objects.get(pk=book_id)
        except cls.DoesNotExist:
            return None

    @property
    def background_filepath(self) -> str:
        return 'book' + str(random.randint(1, BOOK_SPINES_QUANTITY)) + '.png'

    @property
    def title_preview(self) -> str:
        return self.title if len(self.title) <= 43 else f'{self.title[:40].rstrip()}...'

    @property
    def author_preview(self) -> str:
        author_name = self.author_full_name
        return author_name if len(author_name) <= 48 else f'{author_name[:45].rstrip()}...'
