from django.contrib import admin
from django.db.models import TextField
from tinymce.widgets import TinyMCE
from django_summernote.admin import SummernoteModelAdmin
from .models import Gamebook_art, carousel
from django import forms
from ckeditor.widgets import CKEditorWidget
# Register your models here.
class SomeModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'

class slugify(admin.ModelAdmin):
    readonly_fields = ['slug']

admin.site.register(Gamebook_art, slugify)
admin.site.register(carousel, SomeModelAdmin)
admin.site.site_header = "Gamebook Admin"
admin.site.site_title = "Gamebook Admin"
