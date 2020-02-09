from django.db import models

class Pokemon(models.Model):
    name = models.CharField(max_length=50, unique=True)
    date_added = models.DateField(auto_now_add=True)
    pokeapi_url = models.URLField()
