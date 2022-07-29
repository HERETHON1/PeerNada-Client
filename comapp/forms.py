from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import  FreePost, FreeComment, User, Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__' # 전체 값 입력
    #   fields = ['title', 'body'] # 특정 값만 입력받고 싶을 때

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment'] 

class FreePostForm(forms.ModelForm):
    class Meta:
        model = FreePost
        fields = ['title', 'body'] # 특정 값만 입력받고 싶을 때

class FreeCommentForm(forms.ModelForm):
    class Meta:
        model = FreeComment
        fields = ['comment'] 

class PostSearchForm(forms.Form):
    search_word = forms.CharField(label='Search Word')

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        #username, id,email, mbti,meeting,feedback,ongoing,info,main_act
        fields = ('username', 'id', 'email', 'mbti', 'meeting' ,'feedback','ongoing','info','main_act')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('username', 'id', 'email', 'mbti', 'meeting' ,'feedback','ongoing','info','main_act')

    def clean_password(self):
        return self.initial["password"]