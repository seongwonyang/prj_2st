from django.db import models

# Create your models here.
class Category(models.Model):
    c_id = models.IntegerField(primary_key=True)
    c_code = models.CharField(max_length=100, blank=True, null=True)
    c_name = models.CharField(max_length=100, blank=True, null=True)
    i_code = models.CharField(max_length=100, blank=True, null=True)
    i_name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.c_name

class Product(models.Model):
    p_id = models.IntegerField(primary_key=True)
    c_id = models.ForeignKey('Category', on_delete=models.CASCADE, db_column='c_id')
    p_name = models.CharField(max_length=100, blank=True, null=True)
    img_src = models.URLField('img_src', unique=True)
    price = models.IntegerField(null=True)
    link = models.URLField('link', unique=True)

    def __str__(self):
        return self.p_name