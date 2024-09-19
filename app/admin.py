from django.contrib import admin

from modeltranslation.admin import TranslationAdmin

from .models import Form
# Register your models here.


@admin.register(Form)
class FormAdmin(TranslationAdmin):
    ...