from .models import *

from modeltranslation.translator import TranslationOptions, translator, register



class NewTranslation1(TranslationOptions):
    fields = ('title', 'body')


@register(Products)
class NewTranslation2(TranslationOptions):
    fields = ('title', 'body')


@register(ProductItems)
class NewTranslation3(TranslationOptions):
    fields = ('title', 'body')


@register(WhyUs)
class NewTranslation4(TranslationOptions):
    fields = ('title', 'body')



@register(Oav)
class NewTranslation5(TranslationOptions):
    fields = ('title_1', 'body_1', 'title_2', 'body_2')


class NewTranslation6(TranslationOptions):
    fields = ('title', 'body')


translator.register(Main, NewTranslation1)
translator.register(Aboutus, NewTranslation6)