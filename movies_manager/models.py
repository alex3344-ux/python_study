from django.db import models

# Create your models here

class Director(models.Model):
    """
    Args:
    name = (models.CharField):'Режисер'
    last_name = (models.CharField):'Фамилия'
    email = (models.EmailField):'E-mail'
    """

    first_name = models.CharField('Имя', max_length=100, default="", null=False, db_index=True)
    last_name = models.CharField('Фамилия', max_length=100, default="", null=False, db_index=True)
    email = models.EmailField('E-mail', null=True, db_index=True)

    def __str__(self):
        return f'{self.first_name} - {self.last_name}'

    class Meta:
        verbose_name = 'Режисер'
        verbose_name_plural = 'Режисеры'
        ordering = ['first_name']

class Movie(models.Model):
    """
    Класс описывает таблицу фильма
    
    Args:
        name (models.CharField): 'Наименование фильма'
        rating (models.IntegerField): 'Рейтинг'
        description (models.TextField): 'Описание'
        created_on (models.DateTimeField): 'Создано'
        published_on (models.DateTimeField): 'Опубликовано'
    """
    name = models.CharField('Наименование фильма', max_length=250, blank=True, default='')
    rating = models.IntegerField('Рейтинг', blank=True, default=1, db_index=True)
    description = models.TextField('Описание', blank=True)
    created_on = models.DateTimeField('Создано', auto_now_add=True, db_index=True)
    published_on = models.DateTimeField('Опубликовано', auto_now=True, db_index=True)
    director = models.ForeignKey(Director, on_delete=models.PROTECT, null=True)
    
    def __str__(self) -> str:
        return f'{self.name} - {self.rating}%'

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'
        ordering = ['-published_on']


