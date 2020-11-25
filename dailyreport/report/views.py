from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Work
from .forms import WorkForm, UserRegisterForm
import datetime
from django.contrib import messages
from django.contrib.auth import logout as django_logout
from django.contrib.auth.models import User,auth

# Create your views here.
def index(request):
    return render(request,'index.html')

def create(request):
    allwork = Work.objects.all().order_by('-id')[:5] 
    return render(request,'create.html',{'datas':allwork})

def addWork(request):
    print("hello")
    content = request.POST['detail']
    date = datetime.datetime.now()
    create_at = datetime.datetime.now()
    update_at = datetime.datetime.now()
    insert = Work(content=content,date=date,create_at=create_at,update_at=update_at)
    insert.save()
    return redirect(create)
      
def show(request):
    allwork = Work.objects.all().order_by('-id')
    return render(request,'show.html',{'datas':allwork})

def update_view(request,wid):
    
    instance = get_object_or_404(Work, id=wid)
    form = WorkForm(request.POST or None, instance=instance)
    print(wid)
    if form.is_valid():
        instance = form.save()
        instance.save()
        return redirect(show)
    print(wid)

    # now = datetime.date.today()
    context = {
        "data": instance.date,
        "content": instance.content,
        "update_at": instance.update_at,
        "form":form,
    }
    print(instance.update_at)
    return render(request,"update_view.html",context)

def delete_view(request,wid):
    work = Work.objects.get(id=wid)
    work.delete()
    return render(request,"index.html")

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account ceate for {username} !')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request,'register.html',{'form':form})

def logout(request):
    django_logout(request)
    # return render(request,'logout.html')
    return redirect("login")

def profile(request):
    return render(request,'profile.html')


############################# NOT USE #############################
def update(request,wid):  #not use
    allwork = Work.objects.filter(id=wid)
    return render(request,'update.html',{'datas':allwork})