from django.urls import path, include
from . import views
from django_registration.backends.one_step.views import RegistrationView
from .forms import PollingRegistrationForm

urlpatterns = [
    path("register/", RegistrationView.as_view(form_class=PollingRegistrationForm), name="django_registration_register"),
    path("", include("django_registration.backends.one_step.urls")),
    path('', include("django.contrib.auth.urls")),
    path('profile/', views.profile, name="profile"),


]

