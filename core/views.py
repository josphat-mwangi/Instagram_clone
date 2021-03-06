from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm,UserRegistrationForm,ProfileUpdateForm,CommentForm,PostForm
from django.contrib.auth.models import User
from.models import Image,Post,Comments
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# Create your views here.
def home(request):
    photos = Image.objects.all()
    
    return render(request, 'index.html' , {"photos": photos})
def userhome(request):
    photos = Post.objects.all()
    
    return render(request, 'post.html' , {"photos": photos})


def register(request):
    if request.method == 'POST': #if the form has been submitted
        form = UserRegistrationForm(request.POST) #form bound with post data
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'profile.html', context)

def search(request):
            
    if 'search' in request.GET and request.GET['search']:
        search_term = request.GET.get('search')
        profiles = Profile.search_profile(search_term)
        message = f'{search_term}'

        return render(request, 'search.html',{'message':message, 'profiles':profiles})
    else:
        message = 'Enter term to search'
        return render(request, 'search.html', {'message':message})


class PostListView(ListView):
    model = Post
    template_name = 'post.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_details.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post_form.html' 
    context_object_name = 'posts'
    fields = ['title', 'content','image']
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'post_form.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'post_confirm_delete.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
@login_required (login_url='/accounts/register/')
def add_comment(request,id):
   current_user = request.user
   image = Post.get_single_photo(id=id)
   if request.method == 'POST':
       form = CommentForm(request.POST)
       print(form)
       if form.is_valid():
           comment = form.save(commit=False)
           comment.user = current_user
           comment.image_id = id
           comment.save()
       return redirect('userhome')
   else:
       form = CommentForm()
       return render(request,'new_comment.html',{"form":form,"image":image})    



 
def comments(request,id):
   comments = Comments.get_comments(id)
   number = len(comments   )
   return render(request,'comment.html',{"comments":comments,"number":number})