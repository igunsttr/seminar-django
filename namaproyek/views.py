
from .models import Mahasiswa, Jurusan, Jadwal
from django.shortcuts import render
from django import forms
from .form import Bukutamuform,Bukutamuform2
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
	#POST
	if request.method == 'POST':
		form = Bukutamuform(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')  #jika berhasil disave, redirect ke index
	#GET
	else:
		form = Bukutamuform()
	return render(request, 'bukutamu.html', {'form': form})

def buku_tamu2(request):
	#POST

	if request.method == 'POST':
		form2 = Bukutamuform2(request.POST)
		if form2.is_valid():
			form2.save()
			return redirect('/')  #jika berhasil disave, redirect ke index
	#GET
	else:
		form2 = Bukutamuform2()
	return render(request, 'bukutamu2.html', {'form2': form2})

