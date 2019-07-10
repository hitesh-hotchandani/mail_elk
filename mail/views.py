# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Message


def home(request):
    return HttpResponse("Hello World")


def inbox(request):
    messages = Message.objects.all()
    return render(request, 'mail/inbox.html', {'messages': messages})


def view(request, pk):
    message = get_object_or_404(Message, pk=pk)
    return render(request, 'mail/message.html', {'message': message})
