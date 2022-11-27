from django.shortcuts import render
from .forms import AddContact, AddOrders
from .models import *
from django.db.models import Q
from django.utils.translation import gettext_lazy as _


# Create your views here.


def homepage(request):
    mains = Main.objects.all()
    whyus = WhyUs.objects.all()
    aboutus = Aboutus.objects.all()
    print(aboutus)
    clients = Clients.objects.all()
    sitecontact = SiteContac.objects.all()
    products = Products.objects.all()
    success = False
    if request.method == 'POST':
        form = AddContact(request.POST)
        if form.is_valid():
            form.save()
            success = True
    context = {
        'mains': mains,
        'whyus': whyus,
        'aboutus': aboutus,
        'clients': clients,
        'sitecontact': sitecontact,
        'products': products,
        'success': success

    }

    return render(request, 'main/index.html', context)


def mediapage(request):
    oav = Oav.objects.all()
    context = {
        'oav': oav,
    }
    return render(request, 'main/Assets/media.html', context)


def product(request):
    products = Products.objects.all()
    return render(request, 'main/Assets/products.html', {'products': products})


def buildingpage(request, pk):

    try:
        all = ProductItems.objects.filter(group_id=pk)
        if len(all)%2 == 0:
            products = all[:int(len(all)/2)]
            products1 = all[int(len(all) / 2):]
        else:
            products = all[:int((len(all)+1) / 2)]
            products1 = all[int((len(all)+1) / 2):]
        return render(request, 'main/Assets/building.html', {'products': products, 'products1': products1})
    except:
        print('error')
        return render(request, 'main/Assets/building.html')


def buildingdata(request, group_id, pk):
    item = ProductItems.objects.get(id=pk)
    objs = ProductItems.objects.filter(~Q(id=pk), group_id = group_id)

    success = False
    if request.method == 'POST':
        form = AddOrders(request.POST)
        if form.is_valid():
            form.save()
            success = True

    return render(request, 'main/Assets/buildingData.html', {'item': item, 'objs':objs, 'success': success})

def contact(request):
    success = ''
    sitecontact = SiteContac.objects.all()
    if request.method == 'POST':
        form = AddContact(request.POST)
        if form.is_valid():
            form.save()
            success = 'True'
    return render(request, 'main/Assets/contacts.html', {'success': success, 'sitecontact':sitecontact,
                                                         'available_languages': ['en', 'ru', 'uz']})
