from django.shortcuts import render, redirect

# Create your views here.


# def cate_trend(request):
#     return render(request, 'cate_trend.html')

from django.shortcuts import render
from .models import Thumbnail
from .models import Likevideo
# Create your views here.

# 추가
from django.contrib.auth.models import User  # User에 대한 클래스를 가져온다!
from django.contrib import auth  # 계정에대한권한에 관한 내용을 가져온다~


def home(request):
    return render(request, 'home.html')


# 메세지html추가

def correct(request):
    return render(request, 'correct.html')


def uncorrect(request):
    return render(request, 'uncorrect.html')


def unlog(request):
    return render(request, 'unlog')


# 회원가입 함수 추가
def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
            auth.login(request, user)
            return redirect('correct')
        else:
            return redirect('uncorrect')
    return render(request, 'signup.html')


# 로그인 함수 추가
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'unlog.html')
    else:
        return render(request, 'login.html')


# 로그아웃 함수 추가
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    return render(request, 'home.html')


def cate_trend(request):
    thumbnails = Thumbnail.objects.all()
    checkname = 1
    subcategory = '#플랭'
    category = 'trend'
    urlid = 'dd'
    cate_real_name = request.GET.get('sport_category')

    for thumbnail in thumbnails:
        if cate_real_name == 'trend':
            category = '#트렌드운동'
            if thumbnail.cateDetailName == '플랭크':
                checkname = 1
                subcategory = '#플랭크'
                urlid = thumbnail.urlId
                category_filter = thumbnails.objects.filter(CateName)
            elif thumbnail.cateDetailName == 'piyo':
                checkname = 2
                subcategory = '#PiYo'
                urlid = thumbnail.urlId
            elif thumbnail.cateDetailName == '타바타':
                checkname = 3
                subcategory = '#타바타'
                urlid = thumbnail.urlId

    # elif cate_real_name == 'difficulty':
    #     checkname = 4
    #     category = '#난이도별'
    # elif cate_real_name == 'genre':
    #     checkname = 5
    #     category = '#장르'
    # elif cate_real_name == 'guideline':
    #     checkname = 6
    #     category = '#헬스기구사용법'
    # elif cate_real_name == 'sub1':
    #     checkname = 7
    #     category = '#저쩌구별'
    # elif cate_real_name == 'sub2':
    #     checkname = 8
    #     category = '#쟈쩌구별'

    return render(request, 'cate_trend.html',
                  {'thumbnails': thumbnails, 'category': category, 'subcategory': subcategory, 'urlid': urlid,
                   'cate_real_name': cate_real_name})


def cate_trend(request):
    return render(request, 'cate_trend.html')


# 추가합니다.
def cate_place(request):
    return render(request, 'cate_place.html')


def default_detail(request):
    return render(request, 'default_detail.html')


def detail(request):
    like = Likevideo.objects.all()
    check = 0
    if request.method == 'POST' :
        url = request.POST['hi']

    return render(request, 'detail.html', {'url':url, 'likes':like, 'check':check})


def schedule(request):
    return render(request, 'schedule.html')


def help(request):
    return render(request, 'section_set_help.html')


def profile(request):
    return render(request, 'section_set_profile.html')


def setting(request):
    return render(request, 'section_set_setting.html')


def test(request):
    likes = Likevideo.objects.all()

    return render(request, 'test.html', {'Likes':likes})