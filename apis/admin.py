from django.contrib import admin

from django.contrib import admin
from .models import Distrik, Kampung

class tb_distrik(admin.ModelAdmin):
    list_display = ('id_distrik','nama_distrik')
    list_display_links = ('id_distrik','nama_distrik')
    search_fields = ('nama_distrik',)
    list_per_page = 5

class tb_kampung(admin.ModelAdmin):
    list_display = ('id_kampung','distrik','nama_kampung')
    list_display_links = ('id_kampung','distrik','nama_kampung')
    search_fields = ('nama_kampung',)
    list_per_page = 5

admin.site.register(Distrik, tb_distrik)
admin.site.register(Kampung, tb_kampung)
