from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return f'{self.name}'

class Bookmark(models.Model):
    title = models.CharField(max_length = 40)
    url = models.TextField()
    description = models.TextField()
    category = models.ForeignKey(Category, models.CASCADE, null = True)

