from django.db import models

class Recipe(models.Model):
   title = models.CharField(max_length=100, verbose_name='добавьте название блюда')
   description = models.TextField(verbose_name='добавьте описание блюда')

   def __str__(self):
       return self.title

class Ingredient(models.Model):
    UNIT = (
        ('kg', 'kg'),
        ('g', 'g'),
        ('ml', 'ml'),
        ('l', 'l'),
        ('pcs', 'pcs'),
    )
    name = models.TextField(verbose_name='наименование ингредиента', max_length=100)
    quantity = models.PositiveIntegerField(verbose_name='укажите количество')
    unit = models.CharField(verbose_name='выберите ед. измерения', choices=UNIT, max_length=5)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ingredients')

    def __str__(self):
        return f'{self.name} {self.quantity} {self.unit}'


