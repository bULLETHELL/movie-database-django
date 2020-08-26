from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie

# Create your views here.
def homepage(request):
    return HttpResponse("pythonprogramming.net homepage! Wow so #amaze.")

def movie(request, movie_id):
    return render(request = request,
                  template_name="movies/movie_details.html",
                  context = {"movie": Movie.objects.get(id=movie_id)})

      