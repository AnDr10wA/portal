from django import forms
from .models import MessageForum


class MessageForumForm(forms.ModelForm):
    class Meta:
        model = MessageForum
        fields = ['text', 'author', 'topic']
