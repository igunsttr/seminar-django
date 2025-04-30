
from .models import Mahasiswa, Jurusan, Jadwal
from django.shortcuts import render
from django import forms
from .form import Bukutamuform
from django.shortcuts import render, redirect

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


def buku_tamu(request):
	if request.method == 'POST':
		form = Bukutamuform(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')  #jika berhasil disave, redirect ke index
	else:
		form1 = Bukutamuform()
	return render(request, 'bukutamu.html', {'form': form1})

