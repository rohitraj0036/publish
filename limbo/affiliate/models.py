from django.db import models

# Create your models here.
class product(models.Model):
    name          = models.CharField(max_length=60)
    price         = models.IntegerField()
    categories    = models.CharField(max_length=60, default='')
    SubCategories = models.CharField(max_length=60, default='')
    slug          = models.CharField(max_length=130)
    date          = models.DateField()
    image         = models.ImageField(upload_to='product-image', default='')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}'


class article(models.Model):
    title = models.CharField(max_length=60)
    categories = models.CharField(max_length=60, default='')
    slug = models.SlugField(max_length=130)
    date = models.DateField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/{self.slug}'
