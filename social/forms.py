from django import forms # type: ignore
from .models import Post

class PostForm(forms.ModelForm):
    
    body = forms.CharField(label='', widget=forms.Textarea(attrs={
        'rows' : '3', 'placeholder' : 'inshAllah zarabotayet', 'value' : ''
    }))
    class Meta:
        model = Post
        fields = ['body']
