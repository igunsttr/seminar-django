install microsoft VCC terbaru, di https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170
install laragon versi 6, di https://filehippo.com/download_laragon/   (laragon versi 7 keatas adalah berbayar)
install python 3 di laragon, menu 
tentukan direktori proyek, misal di d:/web

-----Laragon Terminal------
cd d:
cd web
pip install django
pip install django-admin
django-admin startproject namaproyek
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
