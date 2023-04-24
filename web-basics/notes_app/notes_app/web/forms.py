from django import forms

from notes_app.web.models import Profile, Note


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class NoteBaseForm(forms.ModelForm):

    class Meta:
        model = Note
        fields = '__all__'
