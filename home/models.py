from django.db import models

CATEGORY_CHOICES = (
    ("Vegetable", "Vegetable"),
    ("Fruit", "Fruit"),
    ("Dairy", "Dairy"),
    ("Meat", "Meat"),
    ("Sugar", "Sugar"),
    ("Bread", "Bread"),
    ("Pre-Packed", "Pre-Packed"),
    ("Can", "Can"),
    ("Misc", "Misc"),
)


class Item(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="item_imgs",
                              blank=True, default="no_image.jpg")
    category = models.CharField(
        max_length=100, choices=CATEGORY_CHOICES, default="Misc")
    price = models.DecimalField(decimal_places=2, max_digits=3000)
    batch = models.IntegerField(blank=True, null=True)
    desc = models.TextField(max_length=300, default="One of PyShop's item")
    slug = models.SlugField(default="change-me", max_length=40)

    def __str__(self):
        return self.name
