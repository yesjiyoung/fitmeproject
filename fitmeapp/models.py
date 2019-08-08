# from django.db import models

# # Create your models here.
from django.db import models

# Create your models here.
class Category(models.Model):
    categorys = models.CharField(max_length=20, unique=True)


class Thumbnail(models.Model):
    cate_number = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    urlId = models.CharField(max_length=100)
    majorTitle = models.CharField(max_length=100)
    subTitle = models.CharField(max_length=100)
    cateName = models.CharField(max_length=100)
    cateDetailName = models.CharField(max_length=100)

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']
    
    
    def __str__(self):
        return self.cateName + " " + self.cateDetailName


    



    