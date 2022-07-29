from django.contrib import admin
from .models import FreeComment, FreePost, Post, Comment
from .models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserChangeForm, UserCreationForm
# Register your models here.
class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('username', 'id', 'email', 'mbti', 'meeting' ,'feedback','ongoing','info','main_act', 'is_admin')
    
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('username', 'id', 'email', 'mbti', 'meeting' ,'feedback','ongoing','info','main_act')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'id', 'email', 'password1', 'password2', 'mbti', 'meeting' ,'feedback','ongoing','info','main_act')}
         ),
    )
    search_fields = ('username',)
    ordering = ('username',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
#admin 사이트에 Post 등록
admin.site.register(Post)

#admin 사이트에 Comment 등록
admin.site.register(Comment)

admin.site.register(FreePost)
admin.site.register(FreeComment)
