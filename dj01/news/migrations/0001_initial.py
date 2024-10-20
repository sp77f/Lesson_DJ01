# Generated by Django 5.1.1 on 2024-10-17 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Название новости')),
                ('short_description', models.CharField(max_length=300, verbose_name='Краткое описание')),
                ('content', models.TextField(blank=True, verbose_name='Новость')),
                ('created_at', models.DateTimeField(verbose_name='Дата публикации')),
            ],
        ),
    ]
