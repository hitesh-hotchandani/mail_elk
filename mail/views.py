# Create your views here.
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect

from mail import models
from .forms import NewMailForm
from .models import Message


def home(request):
    user = request.user
    return render(request, 'mail/User.html', {'user': user})


def inbox(request):
    messages = Message.objects.filter(is_received=True)
    return return_response(request, 'mail/inbox.html', messages)


def view(request, pk):
    message = get_object_or_404(Message, pk=pk)
    return return_response(request, 'mail/message.html', message)


def important(request):
    messages = models.get_important()
    return return_response(request, 'mail/inbox.html', messages)


def starred(request):
    messages = models.get_starred()
    return return_response(request, 'mail/inbox.html', messages)


def drafts(request):
    messages = models.get_drafts()
    return return_response(request, 'mail/inbox.html', messages)


def return_response(request, path, messages):
    return render(request, path, {'messages': messages})


def all_mails(request):
    return None


def compose(request):
    user = User.objects.first()
    if request.method == 'POST':
        form = NewMailForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.content.body = form.data.get('content')

        return redirect('inbox')
    elif request.method == 'GET':
        form = NewMailForm()
    return render(request, 'mail/compose.html', {'form': form})
