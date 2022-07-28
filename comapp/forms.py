from django import forms
from .models import Post, Comment, FreePost, FreeComment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__' # 전체 값 입력
      # fields = ['title', 'body'] # 특정 값만 입력받고 싶을 때

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
