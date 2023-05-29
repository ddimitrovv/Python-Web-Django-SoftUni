from django.shortcuts import render, redirect

from My_Music_app.web.forms import ProfileCreateForm, ProfileDeleteForm, AlbumCreateForm, AlbumEditForm, AlbumDeleteForm
from My_Music_app.web.models import Profile, Album


def get_profile():
    current_profile = Profile.objects.all() or None
    return current_profile


def get_album(pk):
    album = Album.objects.filter(id=pk).get()
    return album


def home_view(request):
    profile = get_profile()
    if profile is None:
        return add_profile(request)

    context = {
        'albums': Album.objects.all(),
        'profile': profile
    }

    return render(request, 'profile/home-with-profile.html', context)


def add_profile(request):
    profile = get_profile()
    if get_profile() is not None:
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
        'profile': profile,
    }

    return render(request, 'profile/home-no-profile.html', context)


def profile_details(request):
    profile = Profile.objects.get()
    albums_count = Album.objects.count()

    context = {
        'profile': profile,
        'albums_count': albums_count
    }

    return render(request, 'profile/profile-details.html', context)


def profile_delete(request):
    profile = Profile.objects.get()
    albums = Album.objects.all()
    if request.method == 'GET':
        form = ProfileDeleteForm(instance=profile)
    else:
        form = ProfileDeleteForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            albums.delete()
            return redirect('home')
    context = {
        'form': form
    }
    return render(request, 'profile/profile-delete.html', context)


def add_album(request):
    if request.method == 'GET':
        form = AlbumCreateForm()
    else:
        form = AlbumCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'form': form
    }
    return render(request, 'album/add-album.html', context)


def details_album(request, pk):
    album = get_album(pk)
    context = {
        'album': album
    }
    return render(request, 'album/album-details.html', context)


def edit_album(request, pk):
    album = get_album(pk)
    if request.method == 'GET':
        form = AlbumEditForm(instance=album)
    else:
        form = AlbumEditForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'form': form
    }
    return render(request, 'album/edit-album.html', context)


def delete_album(request, pk):
    album = get_album(pk)
    if request.method == 'GET':
        form = AlbumDeleteForm(instance=album)
    else:
        form = AlbumDeleteForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'form': form
    }
    return render(request, 'album/delete-album.html', context)
