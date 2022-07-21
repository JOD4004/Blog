from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post,Comment
from django.views.generic.edit import  UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .forms import CommentForm, PostForm
from django.contrib import messages


#Showing the lists/posts
class PostList(LoginRequiredMixin,ListView):
    login_url = 'account/login1'
    model=Post
    template_name='index.html'

    #get some data from post
    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data(**kwargs)
        context['authors'] = Post.objects.only('author')
        return context

    #get data from server(db)
    def get_queryset(self):
        return Post.objects.order_by('-created')

#Showing post details
class PostDetail(LoginRequiredMixin,DetailView):
    model=Post
    template_name='detail.html'
    slug_field='title'
    slug_url_kwarg='title'
    success_url="/"

    
class CommentonPost(LoginRequiredMixin, CreateView):
    model=Comment
    template_name='comment.html'
    success_url = "/"
    form_class=CommentForm
    def dispatch(self, request, *args, **kwargs):
        id=self.kwargs['pk']
        user_comments = Comment.objects.filter(post_id=id,user=self.request.user).first()
        if user_comments:
            messages.info(request,'You have already commented on the post')
            return HttpResponseRedirect("/") 
        return super(CommentonPost, self).dispatch(request, *args, **kwargs)
    def form_valid(self, form):
        form.instance.post_id=self.kwargs['pk']
        form.instance.user=self.request.user
        form.save()
        return super().form_valid(form)


#Updating posts
class UpdatePost(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'post_update.html'
    success_url = "/"
    form_class = PostForm
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            
            return HttpResponseRedirect('detail')
        return super(UpdatePost, self).dispatch(request, *args, **kwargs)
    def form_valid(self,form):
        obj = self.get_object()
        obj.img.delete(False)
        form.save()
        return super().form_valid(form)
    

#Delete Posts
class DeletePost(DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url ="/"
    def dispatch(self, request, *args, **kwargs):
        messages.info(request,'Click Update if you want to delete the post')
        return super(DeletePost, self).dispatch(request, *args, **kwargs)

#Delete Your Comment
class DeleteComment(DeleteView):
    model = Comment
    success_url ="/"
    def get_object(self):
        return Comment.objects.filter(post_id=self.kwargs.get("pk1"), user_id=self.kwargs.get("pk2"))
    def dispatch(self, request,*args, **kwargs):
        obj = self.get_object()
        obj.delete()
        messages.info(request,'Comment deleted')
        return HttpResponseRedirect("/")

#Posting new datas
class PostFormView(LoginRequiredMixin,CreateView):
    model=Post
    form_class = PostForm
    template_name='post.html'
    success_url = "/"
    #validation of posted foorm
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        return super().form_valid(form)

