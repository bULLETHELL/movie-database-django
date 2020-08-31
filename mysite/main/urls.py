from django.urls import path
from . import views


app_name = 'main'  # here for namespacing of urls.

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("movies/<int:movie_id>", views.movie, name="movie"),
    path("new_discussion/", views.new_discussion, name="new_discussion"),
    path("reply_request/", views.reply_request, name="reply_request"),
    path("logout/", views.logout_request, name="logout"),
    path("login/", views.login_request, name="login"),
]