from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Book(models.Model):
    book_cover_image = models.ImageField(upload_to='book_cover_images', default='default_cover_image')
    book_title = models.CharField(max_length=100)
    book_summary = models.TextField(blank=True, null=True)
    total_reads = models.IntegerField(default=0)
    created_on = models.DateField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    author = models.ForeignKey(User, related_name='books', on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return f" {self.author.username} : {self.book_title}"

class Chapter(models.Model):
    chapter_status_choices = [ ('draft', 'DRAFT'),  ('published', 'PUBLISHED')]

    chapter_number = models.IntegerField()
    chapter_title = models.CharField(max_length=100)
    chapter_status = models.CharField(max_length=120, choices = chapter_status_choices)
    number_of_views = models.IntegerField(default = 0)

    book = models.ForeignKey(Book, related_name='chapters', on_delete=models.CASCADE)


    def __str__(self):
        return f" {self.book.book_title} : {self.chapter_number} - {self.chapter_title}"
    
class Comment(models.Model):
    comment_author = models.ForeignKey(User, related_name='comments', on_delete=models.DO_NOTHING)
    comment_text = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f" {self.comment_author} : {self.comment_text} - {self.created_on}"
    