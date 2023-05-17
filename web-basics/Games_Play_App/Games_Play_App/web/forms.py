from django import forms

from Games_Play_App.web.models import Profile, Game


class ProfileCreateForm(forms.ModelForm):
    # password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Profile
        widgets = {
            'password': forms.PasswordInput,
        }
        fields = ('email', 'age', 'password')
        

class GameBaseForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = '__all__'
