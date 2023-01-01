from django import forms
from .models import Poll


class PollCustomForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ['title', 'text', 'slug']

