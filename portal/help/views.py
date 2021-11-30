from django.shortcuts import render, redirect
from django import forms
from .models import HelpMessage
from django.http import HttpResponse


class MessageForm(forms.ModelForm):
    class Meta:
        model = HelpMessage
        fields = '__all__'


def get_message_form(request):
    form = MessageForm()
    return render(request, 'help.html', {'form':form})


def save_form(request):
    form = MessageForm(request.POST)

    if form.is_valid():
        data = form.cleaned_data
        firstname = data.get('firstname')
        surname = data.get('surname')
        email = data.get('email')
        message = data.get('message')
        obj = HelpMessage(firstname = firstname, surname = surname,
                          email = email, message = message)
        obj.save()
    return redirect("/")