from django.shortcuts import render, redirect, get_object_or_404
from .forms import CommentForm, PostForm, FreePostForm, FreeCommentForm
from .models import Post, FreePost, User
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
from django.contrib import auth # auth를 통해 로그인, 로그아웃 기능 구현

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

def poster(request):
    auth.logout(request)
    return render(request, 'poster.html')

def signup(request):
    if request.method == "POST":
        if request.POST['password'] == request.POST['repeat']:
            # 회원가입
            new_user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
            # 로그인
            auth.login(request, new_user)
            # 홈 리다이렉션
            return redirect('home')
    return render(request, 'register.html')

# 메인 페이지
def main_page(request):
    return render(request, 'main_page.html')

# 익명게시판 홈페이지
def home(request):
    return render(request, 'base.html')#'index.html', {'posts':posts})

def postcreate(request):
    # request method가 POST일 경우
    if request.method == 'POST' or request.method == 'FILES':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

    # request method가 GET일 경우
    # form 입력 html 띄우기
    else:
        form = PostForm()
    return render(request, 'post_form.html', {'form':form})

def detail(request):
    # post_detail = get_object_or_404(Post, pk=post_id)
    # comment_form = CommentForm()
    return render(request, 'detail.html')#, {'post_detail':post_detail, 'comment_form':comment_form})

# 댓글 저장
def new_comment(request, post_id):
    filled_form = CommentForm(request.POST)
    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False)
        finished_form.post = get_object_or_404(Post, pk=post_id)
        finished_form.save()
    return redirect('detail', post_id)


# 자유게시판 홈페이지
def freehome(request):
    #posts = Post.objects.all() # post의 모든 객체를 가져와라
    freeposts = FreePost.objects.filter().order_by('-date') # 날짜를 오름차순으로 가져와라 (-date : 내림차순)
    return render(request, 'free_index.html', {'freeposts':freeposts})

def freepostcreate(request):
    if request.method == 'POST' or request.method == 'FILES':
        form = FreePostForm(request.POST, request.FILES)
        if form.is_valid():
            unfinished = form.save(commit=False)
            unfinished.author = request.user            # user 추가!
            unfinished.save()
            return redirect('freehome')
    else:
        form = FreePostForm()
    return render(request, 'free_post_form.html', {'form':form})

def freedetail(request, post_id):
    post_detail = get_object_or_404(Post, pk=post_id)
    comment_form = FreeCommentForm()
    return render(request, 'detail.html', {'post_detail':post_detail, 'comment_form':comment_form})

# 댓글 저장
def new_freecomment(request, post_id):
    filled_form = FreeCommentForm(request.POST)
    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False)
        finished_form.post = get_object_or_404(Post, pk=post_id)
        finished_form.save()
    return redirect('freedetail', post_id)

# 검색 기능
def search(request):
    blogs = Post.objects.all().order_by('-id')

    q = request.POST.get('q', "") 

    if q:
        blogs = blogs.filter(title__icontains=q)
        return render(request, 'search.html', {'blogs' : blogs, 'q' : q})
    
    else:
        return render(request, 'search.html')

def post(request):
    # print("출력")
    # if request.method == "POST":
    #     print("post")
    #     contenttitle = request.POST['contentdetail']
    #     contenturl = request.POST['contenturl']
    #     contentdetail = request.POST['contentdetail']
    #     content = {
    #         'title':contenttitle,
    #         'url':contenturl,
    #         'body':contentdetail,
    #         'user':request.user
    #     }
    #     print("출력")
    #     # post = Post()
    #     # post.title = contenttitle
    #     # post.url = contenturl
    #     # post.body = contentdetail
    #     # post.user = request.user
    #     # print(post)
    #     # post.save()
    #     return redirect('allcontent') #, {'posts':post})
    # else:
        return render(request, 'allcontent.html')


# def allconte
def post(request):
    return render(request, 'allcontent.html')

def profilemodal(request):
    return render(request, 'profilemodal.html')

def addpost(request):
    # if request.method == "POST":
    #     print("post")
    #     contenttitle = request.POST['contentdetail']
    #     contenturl = request.POST['contenturl']
    #     contentdetail = request.POST['contentdetail']
    #     content = {
    #         'title':contenttitle,
    #         'url':contenturl,
    #         'body':contentdetail,
    #         'user':request.user
    #     }
    #     print("출력")
    #     # post = Post()
    #     # post.title = contenttitle
    #     # post.url = contenturl
    #     # post.body = contentdetail
    #     # post.user = request.user
    #     # print(post)
    #     # post.save()
    #     return redirect('allcontent') #, {'posts':post})
    # else:
        now_user = User.objects.all().filter(id=request.user)
        return render(request, 'content.html', {'now_users':now_user})

def create(request):
    if request.method == "POST":
        print("post")
        contenttitle = request.POST['contenttitle']
        contenturl = request.POST['contenturl']
        contentdetail = request.POST['contentdetail']
        
        # content = {
        #     'title':contenttitle,
        #     'url':contenturl,
        #     'body':contentdetail,
        #     'user':request.user
        # }
        post = Post()
        post.title = contenttitle
        post.url = contenturl
        post.body = contentdetail
        post.user = request.user
        print(post)
        post.save()
        return redirect('home') 
