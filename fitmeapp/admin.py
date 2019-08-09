from django.contrib import admin

# 카테고리 모델
from .models import Category
from .models import S_category
from .models import T_category
from .models import Thumbnail

# 사용자 모델
from .models import Likevideo
from .models import Infovideo

# Register your models here.
admin.site.register(Category)
admin.site.register(S_category)
admin.site.register(T_category)
admin.site.register(Thumbnail)

admin.site.register(Likevideo)
admin.site.register(Infovideo)