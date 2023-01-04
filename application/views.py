from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Poll, Choice, Vote
from django.views.generic import ListView, DetailView, CreateView
from .forms import PollCustomForm, ChoiceForm, CommentForm
from django.contrib.auth import logout


# Create your views here.

def logout_view(request):
    logout(request)
    return redirect('poll_list')


class PollingList(ListView):
    model = Poll
    context_object_name = 'polls'
    template_name = 'application/polling_list.html'


class PollingDetailView(DetailView):
    model = Poll
    template_name = 'application/poll_detail.html'
    context_object_name = 'poll'
    form_class = ChoiceForm


# class PollingDetailView1(DetailView):
#     def get(self, request, *args, **kwargs):
#         poll = get_object_or_404(Poll, slug=kwargs['slug'])
#         form_1 = ChoiceForm
#         form_2 = CommentForm
#         context = {'form': form_1, 'comment_form': form_2, 'poll': poll}
#         return render(request, 'application/poll_detail.html', context)
#
#     def post(self, request, *args, **kwargs):
#         poll = get_object_or_404(Poll, slug=kwargs['slug'])
#         form_1 = ChoiceForm(request.POST or None)
#         form_2 = CommentForm(request.POST or None)
#         context = {'form': form_1, 'comment_form': form_2, 'poll': poll}
#         if form_1.is_valid():
#             new_choice = form_1.save(commit=False)
#             new_choice.poll = poll
#             new_choice.save()
#
#         if form_2.is_valid():
#             new_comment = form_2.save(commit=False)
#             new_comment.content_object = poll
#             new_comment.creator = request.user
#
#         return render(request, 'application/poll_detail.html', context)


def detail_view(request, slug):
    user_can_vote = True
    poll = get_object_or_404(Poll, slug=slug)
    if request.user == poll.author:
        choice_form = ChoiceForm(request.POST)
    else:
        choice_form = None
    if request.user.is_anonymous:
        comment_form = None
    else:
        comment_form = CommentForm(request.POST)
    if request.method == "POST":
        if request.user == poll.author:
            choice_form = ChoiceForm(request.POST)
            if choice_form.is_valid():
                choice = choice_form.save(commit=False)
                choice.poll = poll
                choice.save()
                return redirect(request.path_info)
        else:
            choice_form = None
        if request.user.is_anonymous:
            comment_form = None
        else:
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.content_object = poll
                comment.creator = request.user
                comment.save()
                return redirect(request.path_info)

    for vote in poll.votes.all():
        if vote.user == request.user:
            user_can_vote = False
    return render(request, "application/poll_detail.html", {
            "poll": poll,
            "form": choice_form,
            "comment_form": comment_form,
            "user_can_vote": user_can_vote
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


def create_vote(request, slug, pk):

    new_vote = Vote()
    new_vote.poll = Poll.objects.get(slug=slug)
    new_vote.choice = Choice.objects.get(pk=pk)
    new_vote.user = request.user
    new_vote.save()
    return redirect('poll', slug=slug)

