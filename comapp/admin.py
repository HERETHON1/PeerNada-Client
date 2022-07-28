from django.contrib import admin
from .models import FreeComment, FreePost, Post, Comment

#admin 사이트에 Post 등록
admin.site.register(Post)

#admin 사이트에 Comment 등록
admin.site.register(Comment)

admin.site.register(FreePost)
admin.site.register(FreeComment)
