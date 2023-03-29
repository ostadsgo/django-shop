from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=250, db_index=True)
    slug = models.SlugField(max_length=250, unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return str(self.name)


class ProductImage(models.Model):
    product = models.ForeignKey(
        "Product", related_name="images", on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to="images/")


class Product(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    brand = models.CharField(max_length=150, default="un-branded")
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cover = models.ImageField(upload_to="images/")

    def get_absolute_url(self):
        return reverse("product_info", kwargs={"slug": self.slug})
    

    def __str__(self):
        return str(self.title)
