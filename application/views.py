from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Poll, Choice, Vote
from django.views.generic import ListView, DetailView, CreateView
from .forms import PollCustomForm, ChoiceForm, CommentForm


# Create your views here.

class PollingList(ListView):
    model = Poll
    context_object_name = 'polls'
    template_name = 'application/polling_list.html'


class PollingDetailView(DetailView):
    model = Poll
    template_name = 'application/poll_detail.html'
    context_object_name = 'poll'
    form_class = ChoiceForm


class PollingDetailView1(DetailView):
    def get(self, request, *args, **kwargs):
        poll = get_object_or_404(Poll, slug=kwargs['slug'])
        form_1 = ChoiceForm
        form_2 = CommentForm
        context = {'form': form_1, 'comment_form': form_2, 'poll': poll}
        return render(request, 'application/poll_detail.html', context)

    def post(self, request, *args, **kwargs):
        poll = get_object_or_404(Poll, slug=kwargs['slug'])
        form_1 = ChoiceForm(request.POST or None)
        form_2 = CommentForm(request.POST or None)
        context = {'form': form_1, 'comment_form': form_2, 'poll': poll}
        if form_1.is_valid():
            new_choice = form_1.save(commit=False)
            new_choice.poll = poll
            new_choice.save()

        if form_2.is_valid():
            new_comment = form_2.save(commit=False)
            new_comment.content_object = poll
            new_comment.creator = request.user

        return render(request, 'application/poll_detail.html', context)


def detail_view(request, slug):
    poll = get_object_or_404(Poll, slug=slug)
    choice_form = ChoiceForm()
    comment_form = CommentForm()
    if request.method == "POST":
        choice_form = ChoiceForm(request.POST)
        comment_form = CommentForm(request.POST)
        if choice_form.is_valid():
            choice = choice_form.save(commit=False)
            choice.poll = poll
            choice.save()
            return redirect(request.path_info)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.content_object = poll
            comment.creator = request.user
            comment.save()
            return redirect(request.path_info)

    return render(request, "application/poll_detail.html", {
            "poll": poll,
            "form": choice_form,
            "comment_form": comment_form
    })


class PollingCreateView(CreateView):
    model = Poll
    form_class = PollCustomForm
    template_name = 'application/poll_create.html'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.author = self.request.user
        instance.save()
        return redirect('poll', slug=instance.slug)


def create_vote(request, slug, choice):
    poll = get_object_or_404(Poll, slug=slug)
    voting_users = []
    for vote in poll.votes.all:
        voting_users.append(vote.user)
    print(voting_users)

