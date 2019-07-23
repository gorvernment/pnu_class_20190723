from django.db import models

class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    page_url = models.URLField()
    desc = models.TextField(blank=True)

    def __str__(self):
        return self.name