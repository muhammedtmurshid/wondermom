from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.urls import reverse

from core.forms import MotherRegister, BrandRegister, WinForm, ContactForm, VoteForm
from core.models import AwardCategory, VoteBrand, Partners, Win, Vote


def home(request):
    category = AwardCategory.objects.all()
    brands = VoteBrand.objects.order_by('id')[:9]
    partners = Partners.objects.all()
    if request.method == 'POST':
        contactform = ContactForm(request.POST)
        if contactform.is_valid():
            contactform.save()
            return redirect('home')
    else:
        contactform = ContactForm()
    context = {
        'category':category,
        'brands':brands,
        'partners':partners,
        'contactform':contactform,
    }
    return render(request, 'home.html', context)

def mother_register(request):
    if request.method == 'POST':
        motherform = MotherRegister(request.POST)
        if motherform.is_valid():
            motherform.save()
            return redirect('mother_register')
    else:
        motherform = MotherRegister()
    return render(request, 'mother_register.html', {'motherform':motherform})


def brand_register(request):
    if request.method == 'POST':
        brandform = BrandRegister(request.POST)
        if brandform.is_valid():
            brandform.save()
            return redirect('brand_register')
    else:
        brandform = BrandRegister()
    return render(request, 'brand_registration.html', {'brandform':brandform})

def vote_brands(request):
    brands = VoteBrand.objects.all()
    if request.method == 'POST':
        contactform = ContactForm(request.POST)
        if contactform.is_valid():
            contactform.save()
            return redirect('home')
    else:
        contactform = ContactForm()
    return render(request, 'vote_brands.html', {'brands':brands, 'contactform':contactform})


def vote(request, id):
    vote_brands = VoteBrand.objects.get(id=id)
    if request.method == 'POST':
        voteform = VoteForm(request.POST or None)
        if voteform.is_valid():
            voteform.save()
            return redirect(reverse('vote', kwargs={'id': id}))
    else:
        voteform = VoteForm()
    return render(request, 'vote.html', {'vote_brands':vote_brands, 'voteform':voteform})

def win(request):
    if request.method == 'POST':
        winform = WinForm(request.POST)
        if winform.is_valid():
            winform.save()
            return redirect('vote')
    else:
        winform = WinForm()
    return render(request, 'win.html', {'winform':winform})

def category(request):
    category = AwardCategory.objects.all()
    if request.method == 'POST':
        contactform = ContactForm(request.POST)
        if contactform.is_valid():
            contactform.save()
            return redirect('home')
    else:
        contactform = ContactForm()
    return render(request, 'category.html', {'category':category, 'contactform':contactform})

def brand(request):
    brands = VoteBrand.objects.all()
    if request.method == 'POST':
        contactform = ContactForm(request.POST)
        if contactform.is_valid():
            contactform.save()
            return redirect('home')
    else:
        contactform = ContactForm()
    return render(request, 'brand.html', {'brands':brands, 'contactform':contactform})

def featured(request):
    win = Win.objects.all()
    if request.method == 'POST':
        contactform = ContactForm(request.POST)
        if contactform.is_valid():
            contactform.save()
            return redirect('home')
    else:
        contactform = ContactForm()
    return render(request, 'featured.html', {'win':win, 'contactform':contactform})

def about(request):
    if request.method == 'POST':
        contactform = ContactForm(request.POST)
        if contactform.is_valid():
            contactform.save()
            return redirect('home')
    else:
        contactform = ContactForm()
    return render(request, 'about.html', {'contactform':contactform})

def partners(request):
    partners = Partners.objects.all()
    if request.method == 'POST':
        contactform = ContactForm(request.POST)
        if contactform.is_valid():
            contactform.save()
            return redirect('home')
    else:
        contactform = ContactForm()
    return render(request, 'partners.html', {'partners':partners, 'contactform':contactform})

def contact(request):
    if request.method == 'POST':
        contactform = ContactForm(request.POST)
        if contactform.is_valid():
            contactform.save()
            return redirect('home')
    else:
        contactform = ContactForm()
    return render(request, 'contact.html', {'contactform':contactform})

def featured_details(request, id):
    win = Win.objects.get(id=id)
    if request.method == 'POST':
        contactform = ContactForm(request.POST)
        if contactform.is_valid():
            contactform.save()
            return redirect('home')
    else:
        contactform = ContactForm()
    return render(request, 'featured_details.html', {'win':win, 'contactform':contactform})

