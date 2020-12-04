from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from .models import Work, PicWork
from .forms import WorkForm, UserRegisterForm, UserUpdateForm, ProfileUpdateForm, PicWorkForm
from django.forms import modelformset_factory
import datetime
from django.contrib import messages
from django.contrib.auth import logout as django_logout
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from PIL import Image
from django.views.generic import ListView

# Create your views here.
@login_required(login_url='login')
def index(request):
    return render(request,'index.html')

@login_required(login_url='login')
def create(request):
    context={
        'work_form' : WorkForm(),
        'pic_form' : PicWorkForm(request.POST,request.FILES),
        'allwork': Work.objects.all().order_by('-id')[:5]

    }
    if request.method == 'POST':
        work_form = WorkForm(request.POST)
        work_form.save()    
        workid = work_form.save()
        pic_form = PicWorkForm(request.POST,request.FILES)
        print(workid.id ,  workid.content,pic_form)

    if request.method == 'POST' and pic_form.is_valid():
        obj = pic_form.save(commit=False)
        obj2 = PicWork(pic=obj.pic, work=workid)
        if obj2.pic !='':
            obj2.save()
         
    else:
        return render(request,'create.html',context)

    return render(request,'create.html',context)


@login_required(login_url='login')
def show(request):

    picworks = PicWork.objects.all().select_related('work')
    # picworks = PicWork.objects.all()
    for pw in picworks:
        print(pw.id,pw.pic,pw.work.content)    
    work = Work.objects.all().order_by('-id')

    # # context={'pic':pic,'content':content}
    context={'picworks':picworks,'pw':pw,'work':work}
    return render(request,'show.html',context,)
   
@login_required(login_url='login')
def update_view(request,wid):
    
    instance = get_object_or_404(Work, id=wid)
    form = WorkForm(request.POST or None, instance=instance)
    print(wid)
    if form.is_valid():
        instance = form.save()
        instance.save()
        return redirect(show)
    print(wid)
    context = {
        "data": instance.date,
        "content": instance.content,
        "update_at": instance.update_at,
        "form":form,
    }
    print(instance.update_at)
    return render(request,"update_view.html",context)

@login_required(login_url='login')
def delete_view(request,wid):
    work = Work.objects.get(id=wid)
    work.delete()
    return render(request,"index.html")
    
@login_required(login_url='login')
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

@login_required(login_url='login')
def logout(request):
    django_logout(request)
    return redirect("login")

@login_required(login_url='login')
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

