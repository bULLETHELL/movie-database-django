from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout, login, authenticate, update_session_auth_hash
from django.contrib import messages
from .models import Movie, Discussion, User, Comment
from .forms import LoginForm, DiscussionForm, CommentForm

# Create your views here.
def homepage(request):
    return HttpResponse("pythonprogramming.net homepage! Wow so #amaze.")

def movie(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    discussions = Discussion.objects.filter(parent_movie=movie)
    return render(request = request,
                  template_name="movies/movie_details.html",
                  context = {'loginForm': LoginForm, 'discussionForm': DiscussionForm, "movie": movie, "discussions": discussions, "user": request.user,})

def new_discussion(request):
    if request.method == 'POST':
        discussionForm = DiscussionForm(request.POST)
        print(discussionForm)
        if discussionForm.is_valid():
            title = discussionForm.cleaned_data.get('title')
            text = discussionForm.cleaned_data.get('text')
            author = discussionForm.cleaned_data.get('author')
            parent_movie = discussionForm.cleaned_data.get('parent_movie')

            newDiscussion = Discussion(title=title, text=text, author=request.user, parent_movie=Movie.objects.get(pk=parent_movie))
            newDiscussion.save()
        else:
            print(discussionForm.errors)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def reply_request(request):
    if request.method == 'POST':
        commentForm = CommentForm(request.POST)
        if commentForm.is_valid():
            text = commentForm.cleaned_data.get('text')
            author = commentForm.cleaned_data.get('author')
            parent_discussion = commentForm.cleaned_data.get('parent_discussion')

            newComment = Comment(text=text, author=request.user, parent_discussion=Discussion.objects.get(pk=parent_discussion))
            newComment.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def login_request(request):
    if request.method == 'POST':
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Logged in: {username}")
                return redirect('/')

    messages.error(request,
                   f"login failed, the login details provided were either wrong or the given user has not yet been activated, if the latter, contact helpdesk")
    return redirect('main:homepage')

def logout_request(request):
    logout(request)
    return redirect('main:homepage')

      