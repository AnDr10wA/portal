from django.shortcuts import render
from .models import *



def cotalog_view(request):

    cotalog = Category.objects.all()
    return render (request, 'categoty.html', {'cotalog':cotalog})



def category_detail(request, slug):


    product = {'videocard': Videocard, 'block': PowerBlock, }
    cat_detail = product[slug].objects.all()
    return  render(request, 'category_detail.html', {'products': cat_detail})



def product_detail(request, slug, category):

    product = {'videocard': Videocard, 'block': PowerBlock, }
    cat_detail = product[category].objects.filter(slug=slug)
    return render(request, 'product_detail.html', {'products': cat_detail})






