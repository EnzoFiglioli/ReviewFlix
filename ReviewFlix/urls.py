from django.contrib import admin
from django.urls import path
from core.views import home_view, search_view, movie_catalog, MovieDetailView, contacto
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name="home"),
    path('search/', search_view, name="search"),
    path('movies/', movie_catalog, name='movies'),
    path('movies/<int:pk>/', MovieDetailView.as_view(), name='movie-detail'),
    path('contacto/', contacto, name="contacto"),
]