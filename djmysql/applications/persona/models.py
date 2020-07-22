from django.db import models


# Create your models here.
class Person(models.Model):
    """  Modelo para registrar personas """

    full_name = models.CharField(
        'Nombres', 
        max_length=50,
    )
    email = models.EmailField(
        blank=True, 
        null=True
    )
    phone = models.CharField(
        'telefono',
        max_length=15,
        blank=True,
    )

    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
    
    def __str__(self):
        return self.full_name