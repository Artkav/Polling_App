from django.shortcuts import render, HttpResponse
from .models import Poll


# Create your views here.

def polling_list(request):
    polls = Poll.objects.all()

    return render(request, "application/polling_list.html", {"polls": polls})


def detail_view(request, slug):
    poll = Poll.objects.get(slug=slug)
    return render(request, "application/poll_detail.html", {"poll": poll})
