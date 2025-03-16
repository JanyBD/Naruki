from django.shortcuts import render
from django.http import HttpResponse
from shopApp.models import Product, Contacts

# Create your views here.
def index(request):
    product_list = Product.objects.all()
    special_offers = Product.objects.filter(product_is_offer=True)
    my_context = {
        'user' : 'Janely',
        'message' : 'Largo de aquí (¿Por favor?)',
        
        'special_offers' : special_offers,
        'product_list' : product_list,
        
        'special_offers_2' : [ #las listas van con corchetes
            {
                'name'  : 'Mascarilla de algo',
                'cost'  : 16.00,
                'image' : 'shopApp/img/mascarilla.jpg'
            },
            {
                'name'  : 'Figuras de anime',
                'cost'  : 1600.00,
                'image' : 'shopApp/img/figuras_anime.jpg'
            },
            {
                'name'  : 'Laptops',
                'cost'  : 16000.00,
                'image' : 'shopApp/img/laptop.jpg'
            },
            {
                'name'  : 'Mouse',
                'cost'  : 160.00,
                'image' : 'shopApp/img/mouse.jpg'
            },
            {
                'name'  : 'Almohada de Naruto (Ojalá tenerla)',
                'cost'  : 160.00,
                'image' : 'shopApp/img/almohada_naruto.jpg'
            },
        ],
    }
    return render(request, 'shopApp/index.html', context = my_context) #insertamos datos de back endddd

def about(request):
    return render(request, 'shopApp/about.html')

def about(request):
    active_contacts = Contacts.objects.filter(contact_active=True)  
    context = {
        'active_contacts': active_contacts  
    }
    return render(request, 'shopApp/about.html', context=context)