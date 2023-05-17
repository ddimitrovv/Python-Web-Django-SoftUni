from django import forms

from Games_Play_App.web.models import Profile


class ProfileCreateForm(forms.ModelForm):
    # password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Profile
        widgets = {
            'password': forms.PasswordInput,
        }
        fields = ('email', 'age', 'password')
        
