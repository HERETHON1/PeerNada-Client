from django.shortcuts import render, redirect, get_object_or_404
from .forms import CommentForm, PostForm, FreePostForm, FreeCommentForm
from .models import Post, FreePost
from django.core.paginator import Paginator
from django.db.models import Q

# 메인 페이지
def main_page(request):
    return render(request, 'main_page.html')

# 익명게시판 홈페이지
def home(request):
    posts = Post.objects.filter().order_by('-date') # 날짜를 오름차순으로 가져와라 (-date : 내림차순)
    # post : 객체들의 목록 ; 목록을 끊어라 (숫자 : 몇개씩 끊을 것인지)
    paginator = Paginator(posts, 5)
    pagnum = request.GET.get('page')
    posts = paginator.get_page(pagnum)
    return render(request, 'index.html', {'posts':posts})

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

def detail(request, post_id):
    post_detail = get_object_or_404(Post, pk=post_id)
    comment_form = CommentForm()
    return render(request, 'detail.html', {'post_detail':post_detail, 'comment_form':comment_form})

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
    return render(request, 'allcontent.html')