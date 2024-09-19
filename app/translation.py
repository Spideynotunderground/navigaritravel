from modeltranslation.translator import TranslationOptions, register
from .models import Form

@register(Form)
class FormTranslationOptions(TranslationOptions):
    fields = ('name', 'surname', 'country')  # Add fields that require translation
