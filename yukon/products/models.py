from django.db import models
from django.utils import timezone

class Product(models.Model):
    title = models.CharField('Назва товару', max_length=50, default='NoName')
    preview = models.ImageField('Превю товару', upload_to='products/preview')
    description = models.TextField('Опис товару', max_length=1500, default='')
    price = models.IntegerField('Ціна', default=50)
    number = models.IntegerField('Кількість', default=1)
    date = models.DateTimeField('Дата', default=timezone.now)
    category = models.CharField('Категорія', max_length=50, default='uncategorized')
    id = models.AutoField(primary_key=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товари'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            count = Product.objects.count()
            self.id = count + 1
        super().save(*args, **kwargs)
