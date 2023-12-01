from django.contrib import admin

from books.models import Book


@admin.register(Book)
class BooksAdmin(admin.ModelAdmin):
    list_display = [
        "title", "author_full_name", "year_of_publishing", "copies_printed", "description_preview"]

    def description_preview(self, obj: Book) -> str:
        return f"{obj.short_description[:30]}..."
