from .models import Category

def category_shop(request):
    category = Category.objects.all()
    return {"category_shop":category}