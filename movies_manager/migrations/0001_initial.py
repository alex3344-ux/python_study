# Generated by Django 4.1.4 on 2022-12-07 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=250, verbose_name='Наименование фильма')),
                ('rating', models.IntegerField(blank=True, db_index=True, default=1, verbose_name='Рейтинг')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('created_on', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Создано')),
                ('published_on', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Опубликовано')),
            ],
        ),
    ]
