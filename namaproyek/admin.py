from django.contrib import admin
admin.site.site_header = 'Halaman Administrasi'
from .models import  Jurusan, Mahasiswa, Gedung, Ruang, Jadwal, Dosen, Matkul
admin.site.register(Jurusan)
admin.site.register(Mahasiswa)
admin.site.register(Gedung)
admin.site.register(Ruang)
admin.site.register(Jadwal)
admin.site.register(Dosen)
admin.site.register(Matkul)