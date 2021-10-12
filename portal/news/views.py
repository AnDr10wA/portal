from django.shortcuts import render, redirect
from django.views import View
from .models import *
from .utils import *
# from .forms import NewsForm


def news_list(request):
    news = News.objects.all()
    return render(request, 'main.html', {'news':news})


class NewsDetail(ObjectsDetailMixin, View):
    model = News
    template = 'news_detail.html'

# class NewsCreate(View):
#     def get(self, request):
#         form = NewsForm()
#         return render(request, 'news_create.html', {'form':form})
#
#     def post(self, request):
#         bound_form = NewsForm(request.POST)
#         if bound_form.is_valid():
#             news = bound_form.save()
#             return redirect(news)
#         return render(request, 'news_create.html', {'form':bound_form})