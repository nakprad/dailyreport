from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Work, PicWork
from .forms import WorkForm, UserRegisterForm, UserUpdateForm, ProfileUpdateForm, PicWorkForm
from django.forms import modelformset_factory
import datetime
from django.contrib import messages
from django.contrib.auth import logout as django_logout
from django.contrib.auth.models import User,auth

# Create your views here.
def index(request):
    return render(request,'index.html')

def create(request):
    form = PicWorkForm(request.POST or None , request.FILES or None)
    if request.method =='POST':

        content = request.POST['detail']
        date = datetime.datetime.now()
        create_at = datetime.datetime.now()
        update_at = datetime.datetime.now()
        create = Work(content=content,date=date,create_at=create_at,update_at=update_at)
        create.save()
        obj = form.save()
        obj.work = create
        obj.save()


        form = PicWorkForm(request.POST or None , request.FILES or None)
    else:
       pass
    context={
        'form':PicWorkForm(request.POST or None , request.FILES or None)
    }
    return render(request,'create.html',context)

def addWork(request):
    print("create work")
    if request.method == 'POST':
        form = WorkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = WorkForm()
    return redirect(create)

    #     content = request.POST['detail']
    #     date = datetime.datetime.now()
    #     create_at = datetime.datetime.now()
    #     update_at = datetime.datetime.now()
    #     insert = Work(content=content,date=date,create_at=create_at,update_at=update_at)
    #     insert.save()
    # return redirect(create)
      
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
    return redirect("login")

def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance = request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES, instance = request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect(profile)

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form':u_form,
        'p_form':p_form, 

    }
    return render(request,'profile.html',context)

