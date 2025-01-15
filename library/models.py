from django.db import models

class Books(models.Model):
    GENRE_CHOICES = (
        ('фантастика', 'фантастика'),
        ('роман', 'роман'),
        ('детектив', 'детектив'),
        ('психология', 'психология')
    )
    image = models.ImageField(upload_to='books/', verbose_name = 'загрузите фото')
    title = models.CharField(max_length=100, verbose_name= 'напишите название книги')
    description = models.TextField(verbose_name='добавьте описание', blank = True)
    price = models.PositiveIntegerField(verbose_name='укажите цену', default=400)
    created_at = models.DateTimeField(auto_now_add=True)
    genre_choices = models.CharField(max_length=100, choices=GENRE_CHOICES, verbose_name='выберите жанр')
    author_email = models.EmailField(max_length=100, verbose_name="укажите почту автора")
    author = models.CharField(max_length=100, verbose_name='укажите ФИО автора', default='Л.Н.Толстой')
    trailer = models.URLField(verbose_name='укажите ссылку')
    class Meta:
        verbose_name = 'книга'
        verbose_name_plural = 'книги'
    def __str__(self):
        return f'{self.title} - {self.price} сом'



