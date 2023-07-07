from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Movie, Series
from .serializers import MovieSerializer, SeriesSerializer
from rest_framework.decorators import api_view


#MOVIE
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

@api_view(['GET'])
def list_movies(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_movie(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)

@api_view(['GET'])
def get_movies_by_genre(request, genre):
    movies = Movie.objects.filter(genre=genre)
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

#SERIES 

class SeriesViewSet(viewsets.ModelViewSet):
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer

@api_view(['GET'])
def list_series(request):
    series = Series.objects.all()
    serializer = SeriesSerializer(series, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_serie(request, series_id):
    series = get_object_or_404(Series, pk=series_id)
    serializer = SeriesSerializer(series)
    return Response(serializer.data)

@api_view(['GET'])
def get_series_by_rating(request, rating):
    series = Series.objects.filter(rating=rating)
    serializer = SeriesSerializer(series, many=True)
    return Response(serializer.data)