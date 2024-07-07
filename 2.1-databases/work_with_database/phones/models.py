from django.db import models
from django.utils.text import slugify


class Phone(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, verbose_name='Модель телефона')
    price = models.IntegerField(verbose_name='Цена')
    image = models.ImageField(upload_to='', verbose_name='Изображение')
    release_date = models.DateField()
    slug = models.SlugField(blank=True, unique=True, verbose_name='URL')
    lte_exists = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


    def __str__(self):
        return f'{self.id}: {self.name}, {self.release_date}, {self.price}'











    # TODO: Добавьте требуемые поля
    pass
