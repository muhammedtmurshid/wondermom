from django.urls import path

from core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('mother_register/', views.mother_register, name='mother_register'),
    path('brand_register/', views.brand_register, name='brand_register'),
    path('votes/<int:id>/', views.vote, name='vote'),
    path('vote_brands/', views.vote_brands, name='vote_brands'),
    path('win/', views.win, name='win'),
    path('category/', views.category, name='category'),
    path('brand/', views.brand, name='brand'),
    path('featured/', views.featured, name='featured'),
    path('about/', views.about, name='about'),
    path('partners/', views.partners, name='partners'),
    path('contact/', views.contact, name='contact'),
    path('featured_details/<int:id>/', views.featured_details, name='featured_details'),


]