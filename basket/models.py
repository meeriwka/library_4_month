from django.db import models
from library.models import Books

class Basket(models.Model):
   choice_book = models.ForeignKey(Books, on_delete=models.CASCADE)
   comment = models.TextField()
   checked = models.CharField(max_length=20, choices = (('Done', 'Done'), ('Not completed', 'Not completed')))
   created_at = models.DateTimeField(auto_now_add=True)

   def __str__(self):
       return f'{self.created_at} {self.choice_book} {self.checked} {self.comment}'
