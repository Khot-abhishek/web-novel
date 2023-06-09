from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from PIL import Image

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, default='no_category_selected')
    
    def __str__(self):
        return f" {self.name}"

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f" {self.name}"

class Book(models.Model):
    book_cover_image = models.ImageField(upload_to='book_cover_images', default='default_cover_image')
    book_title = models.CharField(max_length=100)
    book_summary = RichTextField()
    total_reads = models.IntegerField(default=0)
    created_on = models.DateField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    author = models.ForeignKey(User, related_name='books', on_delete=models.DO_NOTHING)
    category = models.ForeignKey(Category, related_name='category', on_delete=models.DO_NOTHING)
    tags = models.ManyToManyField(Tag, related_name='tags')

    def __str__(self):
        return f" {self.author.username} : {self.book_title}"

    def get_tags(self):
        all_tags = self.tags.all()
        return all_tags

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.book_cover_image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.book_cover_image.path)




class Chapter(models.Model):
    chapter_status_choices = [ ('draft', 'DRAFT'),  ('published', 'PUBLISHED')]

    chapter_number = models.IntegerField()
    chapter_title = models.CharField(max_length=100)
    chapter_body = RichTextField()
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
    