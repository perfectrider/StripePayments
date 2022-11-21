from django.db import models

class Item(models.Model):
    '''Object for payment'''

    name = models.CharField(max_length=100,
                            verbose_name='Наименование')
    description = models.TextField(max_length=300,
                                   verbose_name='Описание')
    price = models.FloatField(default=0,
                              verbose_name='Цена')

    def __str__(self):
        return f"{self.name},  {self.price}"

