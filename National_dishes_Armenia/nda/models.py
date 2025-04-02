from django.db import models


class Dish(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    photo = models.ImageField(upload_to="photos/%Y/%m/%d")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    cat = models.ForeignKey('DishCategory', on_delete=models.CASCADE)
    recipe = models.ForeignKey('Recipes', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class DishCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.quantity} {self.name}"


class Recipes(models.Model):
    ingredients = models.ManyToManyField('Ingredient')
    description = models.TextField()
    cooking_time = models.TimeField()

    def __str__(self):
        return self.ingredients
