from .models import Category


def get_category(request):
    all_cats = Category.objects.all()
    return {'all_categories': all_cats}