from django.db import models


class Category(models.Model):
    title = models.TextField(max_length=255, default="test")
    description = models.TextField(default="test description", blank=True)

    def __str__(self):
        return self.title
    
