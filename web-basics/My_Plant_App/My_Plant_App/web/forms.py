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
    ...

# ----- Plant Forms -----


class PlantBaseForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = '__all__'


class PlantCreateForm(PlantBaseForm):
    ...


class PlantDetailsForm(ProfileBaseForm):
    ...


class PlantEditForm(ProfileBaseForm):
    ...


class PlantDeleteForm(ProfileBaseForm):
    ...
