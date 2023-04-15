from django.contrib import admin
from .models import Book, Chapter, Comment

# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('book_title', 'book_summary', 'author')
    search_fields = ('book_title', 'author', 'created_on','updated_on')
    list_filter = ('total_reads','created_on', 'updated_on')

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ('chapter_number','chapter_title','chapter_status')
    search_fields = ('chapter_number','chapter_title','chapter_status')
    list_filter = ('chapter_status',)

    class Meta:
        verbose_name = 'Chapter'
        verbose_name_plural = 'Chapters'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment_author','comment_text','created_on')
    search_fields = ('comment_author','comment_text','created_on')
    list_filter = ('created_on',)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'