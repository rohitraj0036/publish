from django.contrib.sitemaps import Sitemap
from .models import product , article


class product_sitemap(Sitemap):

    def items(self):
        return product.objects.all()

class article_sitemap(Sitemap):

    def items(self):
        return article.objects.all()
