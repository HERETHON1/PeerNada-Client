from django.shortcuts import render, redirect
from django.contrib import auth # auth를 통해 로그인, 로그아웃 기능 구현
from django.contrib.auth.models import User
from .models import Profile

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(request, username=username, password=password)
    
        # 실제로 장고 안에 존재하는 회원이라면 로그인 해주기
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else: 
            return render(request, 'bad_login.html')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')

def signup(request):
    if request.method == "POST":
        if request.POST['password'] == request.POST['repeat']:
            # 회원가입
            new_user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
            # 로그인
            auth.login(request, new_user)
            # 홈 리다이렉션
            return redirect('user_info')
    return render(request, 'register.html')

# 사용자 정보 (필수)
def user_info(request):
    return render(request, 'user_info.html')

# 사용자 정보 (선택)
def user_info_select(request):
    return render(request, 'user_info_select.html')

# 회원가입 완료
def sign_finish(request):
    return render(request, 'sign_finish.html')

# 마이페이지
def profile(request):
    profile_info = Profile.objects.filter(user_id=request.user) #특정 user_id로 .. 아마 request.user 같은 거로 바꾸면 될 듯
    return render(request, "mypage.html", {'profile_infos':profile_info})

# 마이페이지 수정
def profile_mod(request):
    return render(request, "profile_mod.html")