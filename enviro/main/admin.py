from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin
# Register your models here

admin.site.register(Main)
admin.site.register(Products)
admin.site.register(ProductItems)
admin.site.register(WhyUs)
admin.site.register(Oav)
admin.site.register(Contact)
admin.site.register(Orders)
admin.site.register(Aboutus)
admin.site.register(Clients)
admin.site.register(SiteContac)
