from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    parent = models.ForeignKey('self',  null=True, blank=True, related_name='children', on_delete=models.CASCADE)


    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Good(models.Model):
    category = models.ForeignKey(Category, related_name='goods', on_delete=models.CASCADE)
    name = models.CharField(max_length=50, db_index=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.PositiveIntegerField()
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)



    class Meta:
        ordering = ('name',)
        index_together = ('id',)

    def __str__(self):
        return self.name


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    publish_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    good = models.ForeignKey(Good, on_delete=models.CASCADE)

    def __str__(self):
        return self.content
