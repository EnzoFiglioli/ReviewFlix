from django.views.generic import DetailView
from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie
from django.contrib import messages
from django.core.mail import EmailMessage

def home_view(request):
    latest_movies = Movie.objects.order_by('-created_at')[:5]
    context = {
        'latest_movies': latest_movies
    }
    return render(request, 'core/home.html', context)

def movie_catalog(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies
    }
    return render(request, 'core/movies.html', context)

def search_view(request):
    query = request.GET.get('q')
    if query is not None:
        movie_results = Movie.objects.filter(title__icontains=query)
        results = list(movie_results)
    else:
        results = []
    
    context = {
        'query': query,
        'results': results
    }
    return render(request, 'core/search.html', context)

class MovieDetailView(DetailView):
    model = Movie
    template_name = 'core/movie_detail.html'
    context_object_name = 'movie'
from .forms import Contact

def contacto(request):
    if request.method == 'POST':
        form = Contact(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            correo = form.cleaned_data['correo']
            mensaje = form.cleaned_data['mensaje']

            subject = f'Mensaje de {nombre}'
            content = mensaje

            destinatario = EmailMessage(subject, content, to=[correo])
            destinatario.send()

            

            return redirect('home')
    else:
        form = Contact()

    return render(request, 'core/contact.html', {'form': form})
