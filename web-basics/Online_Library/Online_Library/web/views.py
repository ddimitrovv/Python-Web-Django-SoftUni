from http.client import HTTPResponse

from django.shortcuts import render, redirect

from Online_Library.web.forms import ProfileBaseForm, BookBaseForm, ProfileDeleteForm
from Online_Library.web.models import Profile, Book


def get_profile():
    current_profile = Profile.objects.all() or None
    return current_profile


def add_profile(request):
    current_profile = get_profile()
    if current_profile is not None:
        return redirect('home')

    if request.method == 'GET':
        form = ProfileBaseForm()
    else:
        form = ProfileBaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'form': form,
    }

    return render(request, 'home-no-profile.html', context)


def profile_edit(request):
    curren_profile = Profile.objects.get()
    if request.method == 'GET':
        form = ProfileBaseForm(instance=curren_profile)
    else:
        form = ProfileBaseForm(request.POST, instance=curren_profile)
        if form.is_valid():
            form.save()
            return redirect('profile details')

    context = {
        'profile': curren_profile,
        'form': form
    }

    return render(request, 'edit-profile.html', context)


def profile_delete(request):
    curren_profile = Profile.objects.get()
    if request.method == 'GET':
        form = ProfileDeleteForm(instance=curren_profile)
    else:
        form = ProfileDeleteForm(request.POST, instance=curren_profile)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'profile': curren_profile,
        'form': form
    }

    return render(request, 'delete-profile.html', context)


def profile_details(request):
    current_profile = Profile.objects.get()
    context = {
        'profile': current_profile
    }
    return render(request, 'profile.html', context)


def home_view(request):
    current_profile = get_profile()
    if current_profile is None:
        return add_profile(request)

    context = {
        'profile': Profile.objects.get(),
        'books': Book.objects.all(),
    }

    return render(
        request, 'home-with-profile.html', context,
    )


def add_book(request):
    current_profile = Profile.objects.get()
    if request.method == 'GET':
        form = BookBaseForm()
    else:
        form = BookBaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'profile': current_profile,
        'form': form
    }
    return render(request, 'add-book.html', context,)
