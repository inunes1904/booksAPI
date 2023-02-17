from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=5, default=1.99)
    iventory = models.IntegerField(default=1)

    def __str__(self):
        return self.title + ' by ' + self.author