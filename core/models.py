from django.db import models

# Create your models here.

class AwardCategory(models.Model):
    slno = models.IntegerField()
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media/AwardCategory')

    def __str__(self):
        return self.name

class RegistrationBrandCategory(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class VoteBrand(models.Model):
    slno = models.IntegerField()
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class MotherRegistration(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    category = models.ForeignKey(AwardCategory, on_delete=models.CASCADE)
    socialmedialink = models.URLField()
    about = models.TextField()
    subject = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class BrandRegistration(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    category = models.ForeignKey(RegistrationBrandCategory, on_delete=models.CASCADE)
    socialmedialink = models.URLField()
    about = models.TextField()
    subject = models.CharField(max_length=255)
    def __str__(self):
        return self.name


class Vote(models.Model):
    vote_brands = models.ForeignKey(VoteBrand, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    brand = models.ForeignKey(RegistrationBrandCategory, on_delete=models.CASCADE)
    socialmedialink = models.URLField()
    about = models.TextField()
    subject = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Win(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    socialmedialink = models.URLField()
    about = models.TextField()


    def __str__(self):
        return self.name


class Partners(models.Model):
    image = models.ImageField(upload_to='media/Partners')



class ContactSubject(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    subject = models.ForeignKey(ContactSubject, on_delete=models.CASCADE)
    message = models.TextField()
    def __str__(self):
        return self.name