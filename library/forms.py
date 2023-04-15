from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Book, Chapter, Comment


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ['book_cover_image','book_title','book_summary']


class ChapterForm(forms.ModelForm):
    class Meta:
        model = Chapter
        fields = ['chapter_number','chapter_title','chapter_body','chapter_status']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_author','comment_text']