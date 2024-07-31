from django.db import models

# Criando uma models para o generos
class Genre(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
