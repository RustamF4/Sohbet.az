from django.shortcuts import render # type: ignore
from django.views import View # type: ignore
from .models import Post, Comments
from .forms import PostForm, CommentForm
from social import models
from django.http import HttpResponseRedirect # type: ignore

class PostView(View):
    def get (self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('-created_on')
        form = PostForm()

        context = {'post_list' : posts,
                   'form' : form,
        }


        return render(request, 'social/post_list.html', context)
        
    def post (self, request, *args, **kwargs):

        # posts = Post.objects.all().order_by('-created_on')
        current_user = request.user
        form = PostForm(request.POST)

        if form.is_valid():
            new_post = form.save(False)
            new_post.author = current_user
            new_post.save()

        # context = {'post_list' : posts,
        #            'form' : form,
        # }


        return HttpResponseRedirect(self.request.path_info)
    
class PostDetailView(View):
    def get(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk = pk)
        form = CommentForm()
        comments = Comments.objects.all().order_by('-created_on')
        

        context = {
            'post' : post,
            'form' : form,
            'comments': comments
        }

        return render(request, 'social/post_detail.html', context)
    
    def comment_post(self, request, *args, **kwargs):
        
        current_user = request.user
        comment = CommentForm(request.POST)

        if comment.is_valid():
            new_comment = comment.save(False)
            new_comment.author = current_user
            new_comment.save()

        # context = {'comment_list' : comments,
        #            'comment' : comment,
        # }


        return HttpResponseRedirect(self.request.path_info, )
    
