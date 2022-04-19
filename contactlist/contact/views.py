from django.shortcuts import render, redirect
from .models import contact

# Create your views here.
def index(request):
    contacts = contact.objects.all()
    search_input = request.GET.get('search-area')
    if search_input:
        contacts =contact.objects.filter(full_name__icontains=search_input)
    else:
        contacts = contact.objects.all()
        search_input=''
    context={
        'contacts':contacts,
        'search_input':search_input
    }
    return render(request, 'index.html', context)

def addContact(request):
    if request.method =='POST':
        new_contact = contact(
            full_name = request.POST['fullname'],
            relationship = request.POST['relationship'],
            email = request.POST['email'],
            phone_number = request.POST['phone-number'],
            address = request.POST['address']
        )
        new_contact.save()
        return redirect('/')
    return render(request, 'new.html')

def contactProfile(request, pk):
    contacts = contact.objects.get(id=pk)
    context={
        'contacts':contacts
    }
    return render(request, 'contact-profile.html', context)

def editContact(request, pk):
    contacts = contact.objects.get(id=pk)

    if request.method == 'POST':
        contacts.full_name = request.POST['fullname']
        contacts.relationship = request.POST['relationship']
        contacts.email = request.POST['email']
        contacts.phone_number = request.POST['phone-number']
        contacts.address = request.POST['address']
        contacts.save()
        return redirect('/profile/'+str(contacts.id))
    context={
        'contacts':contacts
    }
    return render(request, 'edit.html', context)

def deleteContact (request, pk):
    contacts = contact.objects.get(id=pk)

    if request.method == 'POST':
        contacts.delete()
        return redirect('/')
    context={
        'contacts':contacts
    }
    return render(request, 'delete.html', context)
