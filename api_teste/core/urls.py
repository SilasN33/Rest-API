from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'movies_overview', views.MovieViewSet, basename='movie')
router.register(r'series_overview', views.SeriesViewSet, basename='series')

urlpatterns = [

    # Movies
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('list-movies/', views.MovieViewSet.as_view({'get': 'list'}), name='list-movies'),
    path('add-movies/', views.MovieViewSet.as_view({'post': 'create'}), name='add-movies'),
    path('update-movies/<int:pk>/', views.MovieViewSet.as_view({'put': 'update'}), name='update-movie'),
    path('delete-movies/<int:pk>/', views.MovieViewSet.as_view({'delete': 'destroy'}), name='delete-movie'),
    path('movies/genre/<str:genre>/', views.get_movies_by_genre, name='get-movies-by-genre'),

    #Series
    path('list-series/', views.SeriesViewSet.as_view({'get': 'list'}), name='list-series'),
    path('add-series/', views.SeriesViewSet.as_view({'post': 'create'}), name='add-series'),
    path('update-serie/<int:pk>/', views.SeriesViewSet.as_view({'put': 'update'}), name='update-serie'),
    path('delete-serie/<int:pk>/', views.SeriesViewSet.as_view({'delete': 'destroy'}), name='delete-serie'),
    path('serie/rating/<str:rating>/', views.get_series_by_rating, name='get-serie-by-rating'),



]
