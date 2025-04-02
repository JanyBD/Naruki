from django.shortcuts import render, redirect
from django.http import HttpResponse
from shopApp.models import Product, Contacts
from shopApp.forms import FormComment, ContactForm

# Create your views here.
def index(request):
    product_list = Product.objects.all()
    special_offers = Product.objects.filter(product_is_offer=True)
    my_context = {
        
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
    active_contacts = Contacts.objects.filter(contact_active=True).order_by("contact_full_name") 
    context = {
        'active_contacts': active_contacts  
    }
    return render(request, 'shopApp/about.html', context=context)

def form_comment(request):
    form = FormComment()
    if request.method == 'POST': 
        form = FormComment(request.POST)
        if form.is_valid():
            print('FORMULARIO VALIDO')
            print('Nombre: ', form.cleaned_data['full_name'])
            print('Email: ', form.cleaned_data['email'])
            print('Comentario: ', form.cleaned_data['comment'])

    return render(request, 'shopApp/form_comment.html', context={'form' : form})

def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('about')
    else:
        form = ContactForm()
    return render(request, 'shopApp/add_contact.html', {'form': form})