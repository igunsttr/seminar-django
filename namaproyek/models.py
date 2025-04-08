from django.db import models

class Jurusan(models.Model):
    no=models.AutoField(auto_created = True, primary_key=True, serialize=True)
    nama=models.CharField(max_length=100, blank=False, null=False)
    def __str__(self):
        return self.nama
    class Meta:
        verbose_name_plural = "Tabel Jurusan"

class Mahasiswa(models.Model):
    no=models.AutoField(auto_created = True, primary_key=True, serialize=True)
    no_ktp=models.CharField(unique=True, max_length=16)
    nama=models.CharField(max_length=100, blank=False, null=False)
    nim=models.CharField(max_length=12, blank=False, null=False) 
    alamat=models.CharField(max_length=100, blank=False, null=False)
    telepon=models.CharField(max_length=12, blank=False, null=False)
    email=models.EmailField(max_length=100, blank=False, null=False)
    status=models.BooleanField(default=0)
    id_jurusan=models.ForeignKey(Jurusan, on_delete=models.CASCADE, blank=True, null=True)
    #poto=models.CharField(max_length=12, blank=False, null=False)

    def __str__(self):
        return self.nama
    class Meta:
        verbose_name_plural = "Tabel Mahasiswa"

class Dosen(models.Model):
    no=models.AutoField(auto_created = True, primary_key=True, serialize=True)
    no_ktp=models.CharField(unique=True, max_length=16)
    nama=models.CharField(max_length=100, blank=False, null=False)
    nidn=models.CharField(max_length=12, blank=False, null=False) 
    alamat=models.CharField(max_length=100, blank=False, null=False)
    telepon=models.CharField(max_length=12, blank=False, null=False)
    email=models.EmailField(max_length=100, blank=False, null=False)
    status=models.BooleanField(default=0)
    id_jurusan=models.ForeignKey(Jurusan, on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return self.nama
    class Meta:
        verbose_name_plural = "Tabel Dosen"


class Gedung(models.Model):
    no=models.AutoField(auto_created = True, primary_key=True, serialize=True)
    nama=models.CharField(max_length=100, blank=False, null=False)
    lokasi=models.CharField(max_length=100, blank=False, null=False)
    def __str__(self):
        return self.nama
    class Meta:
        verbose_name_plural = "Tabel Gedung"


class Ruang(models.Model):
    no=models.AutoField(auto_created = True, primary_key=True, serialize=True)
    nama=models.CharField(max_length=100, blank=False, null=False)
    id_gedung=models.ForeignKey(Gedung, on_delete=models.CASCADE, blank=True, null=True)
    lantai=models.IntegerField(blank=False, null=False)
    def __str__(self):
        return self.nama
    class Meta:
        verbose_name_plural = "Tabel Ruang"

class Matkul(models.Model):
    no=models.AutoField(auto_created = True, primary_key=True, serialize=True)
    nama=models.CharField(max_length=100, blank=False, null=False)
    id_jurusan=models.ForeignKey(Jurusan, on_delete=models.CASCADE, blank=True, null=True)
    sks=models.IntegerField(blank=False, null=False)
    def __str__(self):
        return self.nama
    class Meta:
        verbose_name_plural = "Tabel Matkul"
class Jadwal(models.Model):
    no=models.AutoField(auto_created = True, primary_key=True, serialize=True)
    id_matkul=models.ForeignKey(Matkul, on_delete=models.CASCADE, blank=True, null=True)
    id_dosen=models.ForeignKey(Dosen, on_delete=models.SET_NULL, blank=True, null=True)
    id_ruang=models.ForeignKey(Ruang, on_delete=models.CASCADE, blank=True, null=True)
    id_jurusan=models.ForeignKey(Jurusan, on_delete=models.CASCADE, blank=True, null=True)
    waktu_1=models.TimeField(blank=False, null=False)
    waktu_2=models.TimeField(blank=False, null=False)
    tanggal=models.DateField(blank=False, null=False)

    class Meta:
        verbose_name_plural = "Tabel Jadwal"
