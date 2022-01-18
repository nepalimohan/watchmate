from rest_framework.response import Response
from django.shortcuts import render
from watchlist_app.models import Movie
from watchlist_app.api.serializers import MovieSerializer

def movies_list(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies)
    return Response(serializer.data)

def movies_details(request):
    pass