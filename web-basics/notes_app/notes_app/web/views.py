from django.shortcuts import render, redirect

from notes_app.web.forms import ProfileBaseForm, NoteBaseForm, NoteDeleteForm, ProfileDeleteForm
from notes_app.web.models import Profile, Note


def profile_details(request):
    current_profile = Profile.objects.get()
    len_notes = Note.objects.count()
    print(request)
    context = {
        'profile': current_profile,
        'len_notes': len_notes,
    }
    return render(request, 'profile.html', context)


def delete_profile(request):
    current_profile = Profile.objects.get()
    notes = Note.objects.all()
    current_profile.delete()
    notes.delete()
    return redirect('home')


def add_profile(request):
    current_profile = Profile.objects.all() or None
    if current_profile is not None:
        return redirect('home')

    if request.method == 'GET':
        form = ProfileBaseForm
    else:
        form = ProfileBaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'form': form,
    }

    return render(request, 'home-no-profile.html', context)


def home_view(request):
    current_profile = Profile.objects.all() or None
    if current_profile is None:
        return add_profile(request)

    context = {
        'notes': Note.objects.all(),
    }

    return render(
        request, 'home-with-profile.html', context,
    )


def create_note(request):
    if request.method == 'GET':
        form = NoteBaseForm()

    else:
        form = NoteBaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'form': form
    }
    return render(request, 'note-create.html', context)


def edit_note(request, pk):
    note = Note.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = NoteBaseForm(instance=note)

    else:
        form = NoteBaseForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'form': form,
        'note': note,
    }

    return render(request, 'note-edit.html', context)


def note_details(request, pk):
    note = Note.objects.filter(pk=pk).get()
    context = {
        'note': note
    }
    return render(request, 'note-details.html', context)


def note_delete(request, pk):
    note = Note.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = NoteDeleteForm(instance=note)

    else:
        form = NoteDeleteForm(request.POST, instance=note)
        if form.is_valid():
            note.delete()
            return redirect('home')

    context = {
        'form': form,
        'note': note,
    }

    return render(request, 'note-delete.html', context)
