from django.shortcuts import render, HttpResponse, redirect
from .models import Poll, Choice, Vote
from django.views.generic import ListView, DetailView, CreateView
from .forms import PollCustomForm


# Create your views here.

class PollingList(ListView):
    model = Poll
    context_object_name = 'polls'
    template_name = 'application/polling_list.html'


class PollingDetailView(DetailView):
    model = Poll
    template_name = 'application/poll_detail.html'
    context_object_name = 'poll'


class PollingCreateView(CreateView):
    model = Poll
    form_class = PollCustomForm
    template_name = 'application/poll_create.html'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.author = self.request.user
        instance.save()
        return redirect('poll', slug = instance.slug)
