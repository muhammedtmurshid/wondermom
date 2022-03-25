from django.contrib import admin

# Register your models here.
from core.models import AwardCategory, VoteBrand, RegistrationBrandCategory, MotherRegistration, BrandRegistration, \
    Vote, Partners, Win, ContactSubject, Contact

class AwardCategoryAdmin(admin.ModelAdmin):
    list_display = ['slno', 'name', 'image']

class VoteBrandAdmin(admin.ModelAdmin):
    list_display = ['slno', 'name']


class MotherRegistrationAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'category', 'socialmedialink', 'about', 'subject']


class BrandRegistrationAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'category', 'socialmedialink', 'about', 'subject']



class VoteAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'vote_brands', 'brand', 'socialmedialink', 'about', 'subject']


class WinAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'socialmedialink', 'about']


class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'subject', 'message']

admin.site.register(AwardCategory, AwardCategoryAdmin)
admin.site.register(RegistrationBrandCategory)
admin.site.register(VoteBrand, VoteBrandAdmin)
admin.site.register(MotherRegistration, MotherRegistrationAdmin)
admin.site.register(BrandRegistration, BrandRegistrationAdmin)
admin.site.register(Vote, VoteAdmin)
admin.site.register(Win, WinAdmin)
admin.site.register(Partners)
admin.site.register(ContactSubject)
admin.site.register(Contact, ContactAdmin)

