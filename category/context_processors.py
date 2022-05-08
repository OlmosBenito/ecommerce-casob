from .models import Category


def menu_links(requiest):
    links = Category.objects.all()
    return dict(links=links)