from django import forms

from Games_Play_App.web.models import Profile, Game


class ProfileBaseForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = '__all__'


class ProfileCreateForm(forms.ModelForm):
    # password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        widgets = {
            'password': forms.PasswordInput,
        }
        fields = ('email', 'age', 'password')


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
        

class GameBaseForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = '__all__'


class GameDeleteForm(GameBaseForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance

    def __set_disabled_fields(self):
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = True
            field.required = False
