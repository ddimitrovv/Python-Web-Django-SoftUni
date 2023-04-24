from django.shortcuts import render

from notes_app.web.models import Profile, Note


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist as ex:
        return None


def index(request):
    profile = get_profile()
    if profile is None:
        return render(
            request,
            'home-with-profile.html',
        )  # add_profile(request)

    context = {
        'notes': Note.objects.all(),
    }

    return render(
        request,
        'home-with-profile.html',
        context,
    )
