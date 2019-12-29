from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib import messages
# Create your views here.


def index(request):
    return render(request, 'index.html')


def home(request):
    films = Film.objects.all()
    directors = Director.objects.all()
    return render(request, 'home.html', {'films':films,
                                         'directors': directors})


def add_director(request):
    if request.method == 'POST':
        form = AddDirectorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Director added successfully')
            return redirect('home')
        else:
            messages.error(request, f'Oups something went wrong')

    else:
        form = AddDirectorForm()
    return render(request, 'director/addDirector.html', {'form':form})


def add_film(request):
    if request.method == 'POST':
        form = AddFilmForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f'Film added successfully')
            return redirect('home')
        else:
            messages.warning(request, f'Oups something went wrong')
    else:
        form = AddFilmForm()
    return render(request, 'film/addFilm.html', {'form': form})


def modify_film(request, id):
    film = Film.objects.get(id=id)
    # data = {
    #     'title': film.title,
    #     'release_date': film.release_date,
    #     'description': film.description,
    #     'country': film.country,
    #     'category': film.category
    #     }
    if request.method == 'POST':
        form = FilmUpdateForm(request.POST, request.FILES, instance=film)
        if form.is_valid():
            form.save()
            messages.info(request, f'Film updated')
            return redirect('home')
        else:
            messages.warning(request, f'Oups something went wrong')
    else:
        form = FilmUpdateForm(instance=film)
    return render(request, 'film/film_update.html', {'form':form, 'film':film})


def modify_dir(request, id):
    film = Film.objects.get(id=id)
    director = Director.objects.get(film_id=id)
    if request.method == 'POST':
        form = DirectorUpdateForm(request.POST, instance=director)
        if form.is_valid():
            form.save()
            messages.info(request, f'Director updated')
            return redirect('home')
        else:
            messages.warning(request, f'This director dont want changes')
    else:
        form = DirectorUpdateForm(instance=director)
    return render(request, 'director/dir_update.html',  {'form':form, 'film':film})


def delete_film(request, id):
    if request.method == 'POST':
        old_film = Film.objects.get(id=id)
        old_film.delete()
        return redirect('home')


def comment_film(request, id):
    film = Film.objects.get(id=id)
    comments = Comments.objects.filter(film_id=id)
    summ = 0
    if comments:
        for com in comments:
            sum_rate = summ + com.rating
            summ = sum_rate
        number_of_comments = comments.count()
        final_rate = round(sum_rate/number_of_comments)
        print(final_rate)
    else:
        final_rate = 0

    if request.method == 'POST':
        form = CommentsForm(request.POST)
        if form.is_valid():
            new_com = Comments(
                content=form.cleaned_data['content'],
                rating=form.cleaned_data['rating'],
                user=request.user,
                film=film
                )
            new_com.save()
            messages.success(request, f'Thank you for your comments !')
            return redirect('comment_film', film.id)
        else:
            messages.warning(request, f'Sorry we cannot add your your comment')
    else:
        form = CommentsForm()

    return render(request, 'film/comment_film.html', {'form': form, 'film': film,
                                                      'comments':comments,
                                                      'rate':final_rate})


def delete_comment(request, id):
    old_com = Comments.objects.get(id=id)
    old_com.delete()
    return redirect('home')