from django.shortcuts import render, redirect  # type: ignore
from django.views import View # type: ignore
from .models import Post, Comments, Profile
from .forms import PostForm, CommentForm
from social import models
from django.http import HttpResponseRedirect # type: ignore
from django.views.generic.edit import UpdateView, DeleteView # type: ignore
from django.urls import reverse_lazy # type: ignore
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin # type: ignore

class PostView(View):
    def get (self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('-created_on')
        form = PostForm()

        context = {'post_list' : posts,
                   'form' : form,
        }


        return render(request, 'social/post_list.html', context)
        
    def post (self, request, *args, **kwargs):

        current_user = request.user
        form = PostForm(request.POST)

        if form.is_valid():
            new_post = form.save(False)
            new_post.author = current_user
            new_post.save()

        return redirect('post-list')
    
class PostDetailView(View):
    def get(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk = pk)
        form = CommentForm()
        comments = Comments.objects.filter(post_id = pk).order_by('-created_on')
        

        context = {
            'post' : post,
            'form' : form,
            'comments': comments
        }

        return render(request, 'social/post_detail.html', context)
    
    def post(self, request, pk, *args, **kwargs):
        current_user = request.user
        comment = CommentForm(request.POST)

        if comment.is_valid():
            new_comment = comment.save(False)
            new_comment.author = current_user
            new_comment.post_id = pk
            new_comment.save()


        return HttpResponseRedirect(self.request.path_info, pk)
    

class ProfileView(View):
    def get(self, request, pk, *args, **kwargs):
        user = request.user
        profile = Profile.user
        posts = Post.objects.filter(author = user.id).order_by('-created_on')

        context = {
            'user' : user,
            'profile' : profile,
            'posts' : posts,
        } 

        return render(request, 'social/profile.html', context)
    
   # def post(self, request, pk, *args, **kwargs):
        

       # return HttpResponseRedirect(self.request.path_info)

class ProfileEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Profile
    fields = ['name', 'bio', 'birth_date', 'location', 'profile_picture']
    template_name = 'social/profile_edit.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('profile', kwargs={'pk': pk})

    def test_func(self):
        profile = self.get_object()
        return self.request.user == profile.user