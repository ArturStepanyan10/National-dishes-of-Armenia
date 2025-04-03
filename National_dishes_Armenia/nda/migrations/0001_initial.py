# Generated by Django 5.1.7 on 2025-04-03 19:02

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='Название категории')),
                ('slug', models.SlugField(max_length=255, unique=True, validators=[django.core.validators.MinLengthValidator(5, message='Минимум 5 символов'), django.core.validators.MaxLengthValidator(100, message='Максимум 100 символов')], verbose_name='Слаг')),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('quantity', models.CharField(max_length=50, verbose_name='Количество')),
            ],
        ),
        migrations.CreateModel(
            name='TagPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(db_index=True, max_length=100)),
                ('slug', models.SlugField(max_length=255, unique=True, validators=[django.core.validators.MinLengthValidator(5, message='Минимум 5 символов'), django.core.validators.MaxLengthValidator(100, message='Максимум 100 символов')], verbose_name='Слаг')),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('cooking_time', models.TimeField()),
                ('slug', models.SlugField(max_length=255, unique=True, validators=[django.core.validators.MinLengthValidator(5, message='Минимум 5 символов'), django.core.validators.MaxLengthValidator(100, message='Максимум 100 символов')], verbose_name='Слаг')),
                ('ingredients', models.ManyToManyField(related_name='ingredients', to='nda.ingredient', verbose_name='Ингредиенты')),
            ],
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название блюда')),
                ('description', models.TextField(verbose_name='Описание')),
                ('photo', models.ImageField(blank=True, default=None, null=True, upload_to='photos/%Y/%m/%d', verbose_name='Фото блюда')),
                ('slug', models.SlugField(max_length=255, unique=True, validators=[django.core.validators.MinLengthValidator(5, message='Минимум 5 символов'), django.core.validators.MaxLengthValidator(100, message='Максимум 100 символов')], verbose_name='Слаг')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Время обновления')),
                ('is_published', models.BooleanField(choices=[(False, 'Черновик'), (True, 'Опубликован')], default=0, verbose_name='Статус')),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cats', to='nda.category', verbose_name='Категория')),
                ('recipe', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='recipes', to='nda.recipe', verbose_name='Рецепт')),
            ],
        ),
    ]
