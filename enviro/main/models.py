from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=200)
    number = models.CharField(max_length=200)
    email = models.CharField(max_length=200)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'


class Main(models.Model):
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=200)
    link = models.CharField(max_length=200, default='#')
    image = models.ImageField(default='')
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Main Product'
        verbose_name_plural = 'Main Products'


class Products(models.Model):
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=200)
    icon = models.ImageField()
    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = 'Product Group'
        verbose_name_plural = 'Product Groups'


class ProductItems(models.Model):
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=200)
    image = models.ImageField()
    shape = models.CharField(max_length=50)
    weight = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    packing_specifications = models.CharField(max_length=50)
    group_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Product Item'
        verbose_name_plural = 'Product Items'


class WhyUs(models.Model):
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=200)
    image = models.ImageField()
    klass1 = models.CharField(max_length=200, default='long_content')
    klass2 = models.CharField(max_length=200, default='Why_us_content1')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Why us item'
        verbose_name_plural = 'Why us items'


class Oav(models.Model):
    title_1 = models.CharField(max_length=200)
    body_1 = models.CharField(max_length=200)
    image_1 = models.ImageField()
    title_2 = models.CharField(max_length=200, default='ss')
    body_2 = models.CharField(max_length=200, default='aa')
    image_2 = models.ImageField(default='')

    def __str__(self):
        return self.title_1

    class Meta:
        verbose_name = 'OAV item'
        verbose_name_plural = 'OAV items'


class Aboutus(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'About us item'
        verbose_name_plural = 'About us items'



class Clients(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'


class SiteContac(models.Model):
    number = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = 'Site Kontakti'
        verbose_name_plural = 'Site Kontaktlari'


class Orders(models.Model):
    name = models.CharField(max_length=200)
    number = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    p_title = models.CharField(max_length=200)
    p_body = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'