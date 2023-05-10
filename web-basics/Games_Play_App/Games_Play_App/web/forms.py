from django import forms

from Games_Play_App.web.models import Profile


class ProfileBaseForm(forms.ModelForm):
    # password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Profile
        widgets = {
            'password': forms.PasswordInput,
        }


class NewForm(forms.ModelForm):
    pass
