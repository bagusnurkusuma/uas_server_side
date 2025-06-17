from django.contrib import admin
from .models import Barang,Jenis,About

# Register your models here.
class BarangAdmin(admin.ModelAdmin):
    list_display=('kdbrg','nama','stok','harga', 'jenis_id__nama')
    search_fields=('kdbrg','nama','stok','harga')
    list_filter=('jenis_id__nama',)
    list_per_page= 3
    ordering = ('kdbrg',)

class AboutAdmin(admin.ModelAdmin):
    list_display=('judul','isi')
    search_fields=('judul','isi')
    list_filter=('judul',)
    list_per_page= 3
    ordering = ('judul',)

admin.site.register(Barang, BarangAdmin)
admin.site.register(Jenis)
admin.site.register(About, AboutAdmin)                                                                                            