from django.shortcuts import render

# Create your views here.


# def cate_trend(request):
#     return render(request, 'cate_trend.html')

from django.shortcuts import render
from .models import Thumbnail
# Create your views here.
def home(request):
    return render(request, 'home.html')
def login(request):
    return render(request,'login.html')
def logout(request):
    return render(request,'logout.html')
def signup(request):
    return render(request,'signup.html')
# def cate_trend(request):
#     thumbnails = Thumbnail.objects
#     checkname = 1
#     category = 'trend'
#     cate_real_name = request.GET.get('sport_category')
    
#     if cate_real_name == 'trend':
#         category = '#트렌드운동'
#         if thumbnails.cateDetailName == '플랭크':
#             checkname = 1
#             subcategory = '#플랭크'
#             urlid = thumbnails.urlId
#         elif thumbnails.cateDetailName == 'piyo':
#             subcategory = '#PiYo'
#             urlid = thumbnails.urlId
#         elif thumbnails.cateDetailName == '타바타':
#             subcategory = '#타바타'
#             urlid = thumbnails.urlId

        
#     elif cate_real_name == 'difficulty':
#         checkname = 2
#         category = '#난이도별'
#     elif cate_real_name == 'genre':
#         checkname = 3
#         category = '#장르'
#     elif cate_real_name == 'guideline':
#         checkname = 4
#         category = '#헬스기구사용법'
#     elif cate_real_name == 'sub1':
#         checkname = 5
#         category = '#저쩌구별'
#     elif cate_real_name == 'sub2':
#         checkname = 6
#         category = '#쟈쩌구별'
#     category_filter = thumbnails.objects.filter(cate_number=checkname)
#     return render(request, 'cate_trend.html', 
# {'thumbnails':thumbnails, 'category':category, 'category_filter':category_filter, 'subcategory':subcategory, 'urlid':urlid })

def cate_trend(request):
    return render(request, 'cate_trend.html')


    

#추가합니다.
def cate_place(request):
    return render(request, 'cate_place.html')

def default_detail(request):
    return render(request, 'default_detail.html')

def detail(request):
    return render(request, 'detail.html')

def schedule(request):
    return render(request, 'schedule.html')

def help(request):
    return render(request, 'section_set_help.html')

def profile(request):
    return render(request, 'section_set_profile.html')

def setting(request):
    return render(request, 'section_set_setting.html')


