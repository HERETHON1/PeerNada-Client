from django.contrib import admin
from django.urls import path
from comapp import views
# from accounts import views as accounts_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('allcontent/', views.post, name="allcontent"),
    path('postcreate/', views.postcreate, name='postcreate'),
    path('detail/<int:post_id>', views.detail, name='detail'),
    path('new_comment/<int:post_id>', views.new_comment, name='new_comment'),

    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),    
    # path('profile/', accounts_views.profile, name="profile"),
    # path('profile_mod/', accounts_views.profile_mod, name="profile_mod"),
    
    # 추가 구현 (회원 정보 입력 페이지)
    # path('user_info', accounts_views.user_info, name='user_info'),
    # path('user_info_select/', accounts_views.user_info_select, name='user_info_select'),
    # path('sign_finish/', accounts_views.sign_finish, name='sign_finish'),

    path('main_page/', views.main_page, name='main_page'),

    # 검색 기능
    path('search/', views.search, name='search'),

    path('freehome', views.freehome, name='freehome'),
    path('freepostcreate/', views.freepostcreate, name='freepostcreate'),
    path('freedetail/<int:post_id>', views.freedetail, name='freedetail'),
    path('new_freecomment/<int:post_id>', views.new_freecomment, name='new_freecomment'),


]
