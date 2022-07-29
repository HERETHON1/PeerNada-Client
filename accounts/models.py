# from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# class Profile(models.Model): #그냥 유저로 놔둬도 괜찮을듯
#     # user = models.OneToOneField(settings.AUTH_USER_MODEL)
#     user_id = models.ForeignKey(User, on_delete=models.CASCADE) #나중에 외래키로 변경
#     nickname = models.CharField(max_length=64, blank = False, unique=True, null=True) #나중에 외래키로 변경
#     profile_photo = models.ImageField(blank = True, null=True) #프로필 사진
#     mbti = models.CharField(max_length=4, blank = False, null=True) #mbti
#     keyword1 = models.CharField(max_length=10, blank = False, null=True) #소개 키워드1
#     keyword2 = models.CharField(max_length=10, blank = False, null=True) #소개 키워드2
#     keyword3 = models.CharField(max_length=10, blank = False, null=True) #소개 키워드3
#     info = models.CharField(max_length=50, blank = False, null=True) #한줄 소개
#     main_act = models.CharField(max_length=50, blank = False, null=True) #주요 활동
#     # my_post = models. #내가 쓴 글
#     # my_comment = models. #내가 쓴 댓글

