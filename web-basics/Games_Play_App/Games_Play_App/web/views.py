from django.shortcuts import render, redirect

from Games_Play_App.web.forms import ProfileCreateForm, GameBaseForm
from Games_Play_App.web.models import Profile, Game


def get_profile():
    current_profile = Profile.objects.all() or None
    return current_profile


def add_profile(request):
    current_profile = get_profile()
    if current_profile is not None:
        return redirect('home')

    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'form': form,
    }

    return render(request, 'create-profile.html', context)


def profile_details(request):
    current_profile = Profile.objects.get()
    games = Game.objects.all()
    total_games = games.count()
    total_rating = 0
    for game in games:
        total_rating += game.rating
    average_rating = total_rating / total_games
    context = {
        'profile': current_profile,
        'total_games': total_games,
        'average_rating': average_rating,
    }
    return render(request, 'details-profile.html', context)


def home_view(request):
    current_profile = get_profile()
    if current_profile is None:
        return redirect('add profile')

    context = {
        'profile': Profile.objects.get(),
    }

    return render(
        request, 'home-page.html', context,
    )


def create_game(request):
    if request.method == 'GET':
        form = GameBaseForm()
    else:
        form = GameBaseForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('dashboard')

    context = {
        'form': form
    }
    return render(request, 'create-game.html', context)


def dashboard(request):
    games = Game.objects.all()
    context = {
        'games': games
    }

    return render(request, 'dashboard.html', context)