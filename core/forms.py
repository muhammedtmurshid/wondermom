from django import forms
from django.shortcuts import get_object_or_404

from core.models import MotherRegistration, BrandRegistration, Win, Contact, Vote, VoteBrand


class MotherRegister(forms.ModelForm):
    class Meta:
        model = MotherRegistration
        fields = ('__all__')



class BrandRegister(forms.ModelForm):
    class Meta:
        model = BrandRegistration
        fields = ('__all__')

class VoteForm(forms.ModelForm):
    class Meta:
        model = Vote
        fields = ('name', 'email', 'phone', 'brand', 'socialmedialink', 'about', 'subject')



class WinForm(forms.ModelForm):
    class Meta:
        model = Win
        fields = ('__all__')

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('__all__')