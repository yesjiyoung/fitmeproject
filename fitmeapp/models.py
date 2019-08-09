# from django.db import models

# # Create your models here.
from django.db import models

# Create your models here.
class Category(models.Model):
    categorys = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.categorys

class Thumbnail(models.Model):
    cate_number = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    urlId = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    firstCate = models.CharField(max_length=100)
    secondCate = models.CharField(max_length=100)
    thirdCate = models.CharField(max_length=100)
    videoName = models.CharField(max_length=200, default='')

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']
    
    
    def __str__(self):
        return self.videoName


    



    