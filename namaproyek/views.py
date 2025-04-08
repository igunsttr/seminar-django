
from .models import Mahasiswa, Jurusan, Jadwal
from django.shortcuts import render

def index(request):
	data=Mahasiswa.objects.all()   # query="select * from mahasiswa"
	return render(request, 'index.html', context={'dataku':data})

def about_us(request):
	data=Jurusan.objects.all()
	return render(request, 'aboutus.html', context={'dataku':data})

def portovolio(request):
	data=Mahasiswa.objects.all()
	return render(request, 'portovolio.html', context={'dataku':data})

def contact(request):
	return render(request, 'contact.html')