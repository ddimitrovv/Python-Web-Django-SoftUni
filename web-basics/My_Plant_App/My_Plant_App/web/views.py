from django.shortcuts import render, redirect

from My_Plant_App.web.forms import ProfileCreateForm, PlantCreateForm
from My_Plant_App.web.models import Plant, Profile


def get_profile():
    current_profile = Profile.objects.all() or None
    return current_profile


def get_plant(pk):
    game = Plant.objects.filter(id=pk).get()
    return game


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

    return render(request, 'profile/create-profile.html', context)


def profile_details(request):
    profile = Profile.objects.get()
    plants_count = Plant.objects.all().count()
    context = {
        'profile': profile,
        'plants_count': plants_count
    }
    return render(request, 'profile/profile-details.html', context)


def catalogue(request):
    plants = Plant.objects.all() or None
    context = {
        'plants': plants,
        'profile': Profile.objects.get()
    }
    return render(request, 'catalogue.html', context)


def create_plant(request):
    if request.method == 'GET':
        form = PlantCreateForm()
    else:
        form = PlantCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    context = {
        'form': form,
        'profile': Profile.objects.get()
    }
    return render(request, 'plant/create-plant.html', context)


def details_plant(request, pk):
    plant = Plant.objects.filter(id=pk).get()
    context = {
        'plant': plant,
        'profile': Profile.objects.get()
    }
    return render(request, 'plant/plant-details.html', context)
