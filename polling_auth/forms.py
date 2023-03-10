from django_registration.forms import RegistrationForm
from .models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class PollingRegistrationForm(RegistrationForm):
    class Meta(RegistrationForm.Meta):
        model = User

    def __init__(self, *args, **kwargs):
        super(PollingRegistrationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit("submit", "Register"))
