from django.shortcuts import render, redirect
from .models import BoothList
from .forms import BoothForm, ImageAdd, JoinNew, LoginGo
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
# Create your views here.
def boothlist(request):
    B_list = BoothList.objects.all()
    return render(request, 'booth/list.html', {'list':B_list})

def boothinfo(request,pk):
    info = BoothList.objects.get(pk=pk)
    return render(request, 'booth/info.html', {'info':info})

def boothnew(request):
    if request.method == "POST":
        form = BoothForm(request.POST)
        if form.is_valid():
            booth = form.save(commit=False)
            booth.auther = request.user
            booth.save()
    else:
        form = BoothForm()
    return render(request, 'booth/new.html', {'form':form})

def imgnew(request):
    if request.method == "POST":
        form = ImageAdd(request.POST)
        if form.is_valid():
            booth = form.save(commit=False)
            booth.auther = request.user
            booth.save()
            redirect('booth/')
    else:
        form = ImageAdd()
    return render(request, 'booth/new.html', {'form':form})

def joinsection(request):
    if request.method == "POST":
        form = JoinNew(request.POST)
        if form.is_valid():
            join = User.objects.create_user(**form.cleaned_data)
            login(request,join)
            return redirect('/')
    else:
        form = JoinNew
        return render(request, 'booth/join.html', {'form':form})

def loginsec(request):
    if request.method == 'POST':
        form = LoginGo(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            return HttpResponse('사용자 이름이나 비밀번호가 잘못 되었습니다.')
    else:
        form = LoginGo()
        return render(request, 'booth/login.html',{'form':form})