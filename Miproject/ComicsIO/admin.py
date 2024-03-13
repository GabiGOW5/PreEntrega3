from django.contrib import admin
from .models import *


class ComicAdmin(admin.ModelAdmin):
    list_display = ("comic",)
    list_filter = ("precio", )

admin.site.register(Comic, ComicAdmin)
admin.site.register(el_post)
admin.site.register(OpinionDelComic)
# poner todos los modelos en casa register
# Register your models here.
