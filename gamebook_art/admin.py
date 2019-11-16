from django.contrib import admin
from .models import Gamebook_art, carousel
# Register your models here.
class slugify(admin.ModelAdmin):
    readonly_fields = ['slug']


admin.site.register(Gamebook_art, slugify)
admin.site.register(carousel)
