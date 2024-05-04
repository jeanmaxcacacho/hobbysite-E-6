from django import forms

from .models import Profile

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = [
            "user_name",
            "user_email"
        ]

