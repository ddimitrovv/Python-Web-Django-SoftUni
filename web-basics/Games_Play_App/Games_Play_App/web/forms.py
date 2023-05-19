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


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        

class GameBaseForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = '__all__'


class GameDeleteForm(GameBaseForm):

    class Meta:
        model = Game
        fields = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance

    def __set_disabled_fields(self):
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'
