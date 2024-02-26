"""
Models
"""

from django.db import models

class GuitarModel(models.Model):
    '''
    Model of the guitar
    '''
    manufacturer = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    scale_length = models.FloatField(default=25.5)
    number_of_strings=models.SmallIntegerField(default=6)
    price = models.FloatField()

    main_img = models.ImageField(upload_to='images/', default='Default.png')

    def __str__(self):
        return self.manufacturer + " " + self.model