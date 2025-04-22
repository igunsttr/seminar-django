from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

admin.site.site_header = 'Halaman Administrasi'
from .models import  Jurusan, Mahasiswa, Gedung, Ruang, Jadwal, Dosen, Matkul
#admin.site.register(Jurusan)
admin.site.register(Mahasiswa)
admin.site.register(Gedung)
admin.site.register(Ruang)
admin.site.register(Jadwal)
admin.site.register(Dosen)
admin.site.register(Matkul)

from import_export import resources, widgets, fields
from import_export.admin import ImportExportMixin

class SourceJurusan(resources.ModelResource):
    no=fields.Field(
        column_name='no',
        attribute='no')
    nama=fields.Field(
        column_name='nama',
        attribute='nama')
    class Meta:
        model = Jurusan
        fields = ('no','nama')
class JurusanAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = SourceJurusan
    list_display = ('no','nama')
    search_fields = ['nama']
admin.site.register(Jurusan, JurusanAdmin) 