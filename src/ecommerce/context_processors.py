from .models import Category, Galery, SocialMedia
from django.urls import resolve
def category_shop(request):
    category = Category.objects.all()
    return {"category_shop":category}


def footer(request):
    images = SocialMedia.objects.all()
    images = images[:6] if len(images) == 6 else images[:len(images)] 

    text_about = "Le Lorem Ipsum est simplement du faux texte employé dans la composition et la mise en page avant impression. Le Lorem Ipsum est le faux texte standard de l'imprimerie depuis les années 1500, quand un imprimeur anonyme assembla ensemble des morceaux de texte pour réaliser un livre spécimen de polices de texte. Il n'a pas fait que survivre cinq siècles, mais s'est aussi adapté à la bureautique informatique, sans que son contenu n'en soit modifié. Il a été popularisé dans les années 1960 grâce à la vente de feuilles Letraset contenant des passages du Lorem Ipsum, et, plus récemment, par son inclusion dans des applications de mise en page de texte, comme Aldus PageMaker."

    return {"images_gallery":images,"text_about":text_about}



def current_url_name(request):
    current_url = resolve(request.path_info).url_name
    return {"current_url_name":current_url}