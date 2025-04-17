from django.db import models
from django.urls import reverse


class Product(models.Model):
    name=models.CharField(max_length=200)
    slug=models.SlugField(max_length=200)
    image=models.ImageField(upload_to='picture',blank=True)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse("shop:product_detail", args=[self.id, self.slug])