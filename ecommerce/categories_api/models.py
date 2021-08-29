from django.db import models


class Category(models.Model):
    title = models.TextField(max_length=255, default="Pelotas")
    description = models.TextField(default="", blank=True)

    def __str__(self):
        return self.title
    
