from django.shortcuts import render, redirect

from Games_Play_App.web.forms import ProfileCreateForm
from Games_Play_App.web.models import Profile


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

