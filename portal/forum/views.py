from django.shortcuts import render, get_object_or_404, redirect
from .forms import MessageForumForm
from .models import TopicForum, CategoryForum, MessageForum



def main_view(request):
    categoryes = CategoryForum.objects.all()

    return render(request, 'forum_main.html', {'categoryes': categoryes})

def category_forum_deteil(request, slug):

    category = get_object_or_404(CategoryForum, slug=slug)
    topics = category.topics.all()
    return render(request, 'detail_category_forum.html', {'categoryes': topics})

def topic_detail(request, slug):
    
    topic = get_object_or_404(TopicForum, slug=slug)
    messages = topic.messages.all()
    if request.user.is_authenticated:
        user = request.user
    else:
        user = 'Guest'
    form = MessageForumForm(initial={'author': user, 'topic':topic, 'text': None})

    return render(request, 'topics_detail.html', {'messages': messages, 'form':form})


def save_message(request):
    form = MessageForumForm(request.POST)
    if form.is_valid():
        form.save()
    topic_form = form.cleaned_data['topic']
    topic = TopicForum.objects.get(title = topic_form)


    return topic_detail(request=request, slug = topic.slug)