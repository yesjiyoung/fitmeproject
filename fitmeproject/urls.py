"""fitmeproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path
# import fitmeapp.views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('cate_trend/', fitmeapp.views.cate_trend, name="cate_trend")
# ]


from django.contrib import admin
from django.urls import path, include
import fitmeapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', fitmeapp.views.home, name='home'),
    path('login/', fitmeapp.views.login, name='login'),
    path('logout/', fitmeapp.views.logout, name='logout'),
    path('signup/', fitmeapp.views.signup, name='signup'),
    path('cate_trend/', fitmeapp.views.cate_trend, name='cate_trend'),
    path('cate_place/', fitmeapp.views.cate_place, name='cate_place'),
    path('default_detail/', fitmeapp.views.default_detail, name='default_detail'),
    path('detail/', fitmeapp.views.detail, name='detail'),
    path('schedule/', fitmeapp.views.schedule, name='schedule'),
    path('help/', fitmeapp.views.help, name='help'),
    path('profile/', fitmeapp.views.profile, name='profile'),
    path('setting/', fitmeapp.views.setting, name='setting'),
    path('correct/', fitmeapp.views.correct, name='correct'),
    path('uncorrect/', fitmeapp.views.uncorrect, name='uncorrect'),
    path('unlog/', fitmeapp.views.unlog, name='unlog'),
    path('test/', fitmeapp.views.test, name='test'),

    # path('accounts/', include('allauth.urls')),
]