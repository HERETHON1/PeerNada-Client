from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# 게시물 모델
class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

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
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class FreeComment(models.Model):
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    # 어떤 게시글에 달려 있는 댓글인지 알아야 함 (on_delete : 게시글이 삭제되면 댓글도 같이 삭제됨)
    post = models.ForeignKey(FreePost, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment

