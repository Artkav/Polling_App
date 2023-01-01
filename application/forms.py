from django import forms
from .models import Poll, Choice, Comment, Vote
from crispy_forms.layout import Submit
from crispy_forms.helper import FormHelper


class PollCustomForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ['title', 'text', 'slug']


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['choice_text']

    def __init__(self, *args, **kwargs):
        super(ChoiceForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text']

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))




