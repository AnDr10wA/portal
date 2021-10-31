from django.shortcuts import render, get_object_or_404
from .models import *



def cotalog_view(request):

    cotalog = Category.objects.all()
    return render (request, 'categoty.html', {'cotalog':cotalog})



def category_detail(request, slug):


    product = {'videocard': Videocard, 'block': PowerBlock, 'motherbord': Motherboard,
               'processors': Processor, 'ram': RAMemory}
    cat_detail = product[slug].objects.all()
    return  render(request, 'category_detail.html', {'products': cat_detail})



def product_detail(request, slug, category):
    product = {'videocard': Videocard, 'block': PowerBlock, 'motherbord': Motherboard,
               'processors': Processor, 'ram': RAMemory}
    cat_detail = get_object_or_404(product[category], slug=slug)
    template_name = {'videocard': 'videocard.html','block': 'block.html', 'motherbord': 'motherbord.html',
                     'processors': 'processor.html', 'ram': 'memory.html'}
    return render(request, template_name[category], {'product': cat_detail})



