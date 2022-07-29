from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)

class UserManager(BaseUserManager):
    # user 생성
    def create_user(self, username, id, email, mbti, meeting, feedback, ongoing, info, main_act, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            username=username,
            id=id,
            email=self.normalize_email(email),
            mbti = mbti,
            meeting= meeting,
            feedback=feedback,
            ongoing=ongoing,
            info=info,
            main_act=main_act
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    # super_user 생성
    def create_superuser(self, username, id, email, mbti, meeting, feedback, ongoing, info, main_act, password):
        user = self.create_user(
            username,
            id,
            email,
            mbti ,
            meeting,
            feedback,
            ongoing,
            info,
            main_act,
            password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

# 일반 사용자 사용 model
class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email',
        max_length=255,
        unique=True,
        null=False
    )
    username = models.CharField(max_length=30, unique=True, null=False, default="")
    id = models.CharField(max_length=30, unique=True, null=False, primary_key=True)
    mbti = models.CharField(max_length=5, unique=False, null=True, default="ISTJ")
    meeting= models.BooleanField(unique=False, null=True, editable=True, default=True) #안되면 boolean으로 바꾸기
    feedback=models.BooleanField(unique=False, null=True, editable=True, default=True)
    ongoing=models.BooleanField(unique=False, null=True,editable=True, default=True)
    info=models.CharField(max_length=100, unique=True, null=False)
    main_act=models.CharField(max_length=100, unique=True, null=False)
    is_admin = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = 'id'
    REQUIRED_FIELDS = ['username', 'email', 'mbti', 'meeting' ,'feedback','ongoing','info','main_act']

    def __str__(self):
        return self.id

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

# 게시물 모델
class Post(models.Model):
    title = models.CharField(max_length=200, null=False, unique=True)
    url = models.CharField(max_length=200, null=True, unique=True)
    body = models.TextField(null=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank = False, null=False)
    date = models.DateTimeField(auto_now_add=True,unique=False)
    # 제목이 그대로 보이도록
    def __str__(self):
        return self.title

class Comment(models.Model):
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    # 어떤 게시글에 달려 있는 댓글인지 알아야 함 (on_delete : 게시글이 삭제되면 댓글도 같이 삭제됨)
    post = models.ForeignKey(Post, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment

# 자유 게시판
class FreePost(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class FreeComment(models.Model):
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    # 어떤 게시글에 달려 있는 댓글인지 알아야 함 (on_delete : 게시글이 삭제되면 댓글도 같이 삭제됨)
    post = models.ForeignKey(FreePost, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment
