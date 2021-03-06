from django.db import models
from django.utils.text import Truncator


class Content(models.Model):
    body = models.TextField(max_length=8000, blank=True, default=None)
    attachment = models.TextField(max_length=8000, blank=True, default=None)
    hasAttachment = models.BooleanField(editable=False, default=False)

    # if attachment is not None or attachment is not '':
    #     hasAttachment = True

    def get_body(self):
        return Truncator(self.body).chars(30)

    def __str__(self):
        response = ''
        if self.body is not None:
            response += Truncator(self.body).chars(30) + ' '
        if self.attachment is not None:
            response += Truncator(self.attachment).chars(30) + ' '
        return response
        # if self.hasAttachment is not None:
        #     response += 'True'
        # else:
        #     response += 'False'


# Create your models here.
# def filter_data(field, value):
#     return Message.objects.filter(field, value)


def get_starred():
    return Message.objects.filter(is_starred=True)


def get_important():
    return Message.objects.filter(is_important=True)


def get_drafts():
    return Message.objects.filter(is_sent=False)


class Message(models.Model):
    sender = models.EmailField()
    sender_name = models.CharField(max_length=30, default=sender.__str__())
    to = models.EmailField()
    cc = models.EmailField(blank=True)
    bcc = models.EmailField(blank=True)
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    subject = models.CharField(max_length=1000, blank=True)
    is_read = models.BooleanField(default=False)
    is_starred = models.BooleanField(default=False)
    is_important = models.BooleanField(default=False)
    is_sent = models.BooleanField(default=False)
    is_received = models.BooleanField(default=True)

    def get_sender(self):
        if self.sender.__eq__(self.sender_name):
            return self.sender.__str__()
        return self.sender_name + '<' + self.sender + '>'

    def get_message_subject_render(self):
        return self.subject + ' - <p class="text-muted">' + self.content.body

    @staticmethod
    def get_unread():
        return '(' + Message.objects.filter(is_read=False).count() + ')'

    def __str__(self):
        return self.subject
