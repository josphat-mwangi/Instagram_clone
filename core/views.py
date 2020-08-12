from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm,UserRegistrationForm,ProfileUpdateForm,CommentForm,PostForm
from django.contrib.auth.models import User
from.models import Image,Posts,Comments


# Create your views here.
def home(request):
    photos = Image.objects.all()
    
    return render(request, 'index.html' , {"photos": photos})

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

@login_required (login_url='/accounts/register/')
def comment(request,pk):
    current_user = request.user
    post = Posts.get_single_post(pk)
    comments = Comments.get_post_comment(post.id)
    form = CommentForm(request.POST)
    if request.method == 'POST':
        if form.is_valid:
            comment = form.save(commit=False)
            comment.user = current_user
            comment.post = post
            comment.image_id = post.id
            comment.save()
            return redirect('home')
        else:
            form = NewCommentsForm()
    return render(request, 'comment.html', {"form":form, "post":post, "comments":comments})


@login_required
def posts(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST,files =request.FILES)
        if post_form.is_valid():
            single_post = Posts(user =request.user ,image = request.FILES['image'], description = request.POST['description'] )
            single_post.save()
            messages.success(request, ('Your post was successfully updated!'))
            return redirect(reverse('profiles', kwargs = {'username': request.user.username}))
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        post_form = PostForm()
    return render(request,'post.html', {
        'post_form': post_form
    })