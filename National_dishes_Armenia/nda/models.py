from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models
from django.urls import reverse


class Dish(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'Черновик',
        PUBLISHED = 1, 'Опубликован',

    title = models.CharField(max_length=100, verbose_name='Название блюда')
    description = models.TextField(verbose_name='Описание')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d", default=None, blank=True, null=True,
                              verbose_name='Фото блюда')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="Слаг",
                            validators=[
                                        MinLengthValidator(5, message='Минимум 5 символов'),
                                        MaxLengthValidator(100, message='Максимум 100 символов')
                                    ])
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время обновления')
    is_published = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)),
                                       default=Status.DRAFT, verbose_name='Статус')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='cats', verbose_name='Категория')
    recipe = models.ForeignKey('Recipe', on_delete=models.SET_NULL, null=True, blank=True, default=None,
                               related_name='recipes', verbose_name='Рецепт')

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Название категории')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="Слаг",
                            validators=[
                                MinLengthValidator(5, message='Минимум 5 символов'),
                                MaxLengthValidator(100, message='Максимум 100 символов')
                            ])

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    quantity = models.CharField(max_length=50, verbose_name='Количество')

    def __str__(self):
        return f"{self.name}"


class Recipe(models.Model):
    ingredients = models.ManyToManyField('Ingredient', related_name='ingredients', verbose_name='Ингредиенты')
    description = models.TextField()
    cooking_time = models.TimeField()
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="Слаг",
                            validators=[
                                MinLengthValidator(5, message='Минимум 5 символов'),
                                MaxLengthValidator(100, message='Максимум 100 символов')
                            ])

    def __str__(self):
        return self.slug


class TagPost(models.Model):
    tag = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="Слаг",
                            validators=[
                                MinLengthValidator(5, message='Минимум 5 символов'),
                                MaxLengthValidator(100, message='Максимум 100 символов')
                            ])

    def __str__(self):
        return self.tag

