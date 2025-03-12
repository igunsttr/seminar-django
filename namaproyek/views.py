
from .models import Mahasiswa
from django.shortcuts import render
def index(request):
	data=Mahasiswa.objects.all()
	return render(request, 'index.html', context={'isi':data})