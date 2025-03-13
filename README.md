HOW TO : 
1.install microsoft VCC terbaru, di https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170
2.install laragon versi 6, di https://filehippo.com/download_laragon/   (laragon versi 7 keatas adalah berbayar)
3.install python 3 di laragon, menu 
4. tentukan direktori proyek, misal di d:/web

-----Laragon Terminal------
cd d:
cd web
pip install django
pip install django-admin
django-admin startproject namaproyek
python manage.py makemigrations namaproyek
python manage.py migrate namaproyek
python manage.py createsuperuser
python manage.py runserver
