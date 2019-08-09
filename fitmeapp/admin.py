from django.contrib import admin
from .models import Category
from .models import S_category
from .models import T_category
from .models import Thumbnail
# Register your models here.
admin.site.register(Category)
admin.site.register(S_category)
admin.site.register(T_category)
admin.site.register(Thumbnail)