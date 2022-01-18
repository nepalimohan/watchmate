from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
from watchlist_app.models import Movie
from watchlist_app.api.serializers import MovieSerializer
from django.http import JsonResponse

@api_view(['GET','POST'])
def movies_list(request):
    if request.method == "GET":
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
    
    if request.method == "POST":
        # movies = Movie.objects.all()
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
            

@api_view(['GET','PUT','DELETE'])
def movies_details(request, pk): 
    if request.method == "GET":
        movies = Movie.objects.get(pk=pk)
        serializer = MovieSerializer(movies)
        return Response(serializer.data)
    
    if request_method == "PUT":
        movies = Movie.objects.get(pk=pk)
        # in order to update u need to pass the id so respective value is updated
        serializer = MovieSerializer(movies, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
            
    if request.method == "DELETE":
        pass