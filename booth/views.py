from django.shortcuts import render
from .models import BoothList
from .forms import BoothForm
# Create your views here.
def boothlist(request):
    B_list = BoothList.objects.all()
    return render(request, 'booth/list.html', {'list':B_list})

def boothinfo(request,pk):
    info = BoothList.objects.get(pk=pk)
    return render(request, 'booth/info.html', {'info':info})

def BoothNew(request):
    form = BoothForm()
    return render(request, 'booth/new.html', {'form':form})
