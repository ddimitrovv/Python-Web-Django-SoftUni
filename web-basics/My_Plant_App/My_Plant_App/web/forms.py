from attr.filters import exclude
from django import forms

from My_Plant_App.web.models import Profile, Plant

# ----- Profile Forms -----


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

# ----- Plant Forms -----


class PlantBaseForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = '__all__'


class PlantCreateForm(PlantBaseForm):
    ...


class PlantDetailsForm(PlantBaseForm):
    ...


class PlantEditForm(PlantBaseForm):
    ...


class PlantDeleteForm(PlantBaseForm):
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
