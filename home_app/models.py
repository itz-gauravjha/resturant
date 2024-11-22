from django.db import models
from django.utils.text import slugify
# Create your models here.

class BookTable(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField( max_length=100)
    number = models.IntegerField()
    date = models.DateField()
    person= models.IntegerField()

    def __str__(self):
        return self.name


class Category(models.Model):
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True, blank=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.category_name)
        super(Category, self). save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.category_name
    
    class Meta:
        verbose_name_plural = "Categories"


class MenuItem(models.Model):
    item_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True  , null=True , blank=True)
    category = models.ForeignKey(Category , on_delete=models.CASCADE , related_name="products")
    price = models.IntegerField()
    item_description = models.TextField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.item_name)
        super(MenuItem, self).save(*args, **kwargs)
    
    def __str__(self)->str:
        return self.item_name

    


class MenuItemImage(models.Model):
    menu_item = models.ForeignKey(MenuItem , on_delete=models.CASCADE , related_name="menu_item_images")
    image =  models.ImageField(upload_to="menu_item")