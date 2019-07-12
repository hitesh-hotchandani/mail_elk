from django import forms

from .models import Message


# Message_set = inlineformset_factory(parent_model=Content, model=Message, extra=1)

class NewMailForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(), max_length=8000)

    class Meta:
        model = Message
        fields = ['to', 'cc', 'bcc', 'subject', 'content']
