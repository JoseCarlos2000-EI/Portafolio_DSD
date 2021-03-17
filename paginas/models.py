from django.db import models

# Create your models here.
class usuario (models.Model):
    usuario=models.CharField(max_length=30)
    correo=models.CharField(max_length=60)
    telefono=models.CharField(max_length=60)

    def __str__(self):
        return self.usuario