from django.contrib import admin

# Register your models here.
from .models import Message, Content

admin.site.register(Message)
admin.site.register(Content)
