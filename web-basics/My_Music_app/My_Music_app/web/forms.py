from django import forms

from My_Music_app.web.models import Profile, Album


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileCreateForm(ProfileBaseForm):
    class Meta:
        model = Profile
        exclude = ('profile_picture',)


class ProfileDetailsForm(ProfileBaseForm):
    ...


class ProfileEditForm(ProfileBaseForm):
    ...


class ProfileDeleteForm(ProfileBaseForm):
    class Meta:
        model = Profile
        fields = ()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance


class AlbumBaseForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'


class AlbumCreateForm(AlbumBaseForm):
    ...


class AlbumDetailsForm(AlbumBaseForm):
    ...


class AlbumEditForm(AlbumBaseForm):
    ...


class AlbumDeleteForm(AlbumBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance

    def __set_disabled_fields(self):
        for _, field in self.fields.items():
            field.disabled = True
