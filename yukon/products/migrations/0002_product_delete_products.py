# Generated by Django 4.1.6 on 2023-02-21 21:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('title', models.CharField(default='NoName', max_length=50, verbose_name='Назва товару')),
                ('preview', models.ImageField(upload_to='products/preview', verbose_name='Превю товару')),
                ('description', models.TextField(default='', max_length=1500, verbose_name='Опис товару')),
                ('price', models.IntegerField(default=50, verbose_name='Ціна')),
                ('number', models.IntegerField(default=1, verbose_name='Кількість')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товари',
            },
        ),
        migrations.DeleteModel(
            name='Products',
        ),
    ]
