from django.shortcuts import render # type: ignore
from django.views import View # type: ignore
from .models import Post
from .forms import PostForm
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

        posts = Post.objects.all().order_by('-created_on')
        current_user = request.user
        form = PostForm(request.POST)

        if form.is_valid():
            new_post = form.save(False)
            new_post.author = current_user
            new_post.save()

        context = {'post_list' : posts,
                   'form' : form,
        }


        return HttpResponseRedirect(self.request.path_info)
    
class PostDetailView(View):
    def get(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk = pk)

        context = {
            'post' : post
        }

        return render(request, 'social/post_diteal.html', context)