from django.shortcuts import render, redirect
from phones.models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    if request.GET.get('sort'):
        sort_by = request.GET.get('sort')
        if sort_by == 'min_price':
            phone_objects = Phone.objects.all().order_by('price')
        elif sort_by == 'name':
            phone_objects = Phone.objects.all().order_by('name')
        elif sort_by == 'max_price':
            phone_objects = Phone.objects.all().order_by('-price')
    else:
        phone_objects = Phone.objects.all().values()
    context = {
        'phones': phone_objects
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone_objects = Phone.objects.filter(slug=slug).values()
    context = {
        'phone': phone_objects[0]
    }
    return render(request, template, context)
