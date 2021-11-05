from typing import ContextManager
from django.shortcuts import redirect, render
from.models import Gallery, Reply
from acc.models import User
from django.contrib import messages
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    cate=request.GET.get('cate','sub')
    kw=request.GET.get('kw','')

    if kw:
        if cate == 'sub':
            g=Gallery.objects.filter(subject__startswith = kw)
        elif cate == 'con':
            g=Gallery.objects.filter(content_contains = kw)
        else :
            g=Gallery.objects.filter(writer_startswith  = kw)
    else:
        g=Gallery.objects.all()


    
    page=request.GET.get('page',1)
    pag=Paginator(g,3)
    obj=pag.get_page(page) 
    context={
        'gal':obj,
        'kw':kw,
        'cate':cate
    }
    return render(request,'gallery/index.html',context)

def detail(request,dpk):
    g=Gallery.objects.get(id=dpk)
    r=g.reply_set.all()
    page=request.GET.get('page',1)
    pag=Paginator(r,5)
    obj=pag.get_page(page)

        
    context={
        'gal':g,
        'rep':obj,
        
    }
    return render(request,'gallery/detail.html',context)

def create(request):
    if request.method=='POST':
   
        sub=request.POST.get('subject')
        pic=request.FILES.get('pic')
        con=request.POST.get('content')
       
        if pic and con and sub:
            Gallery(key=request.user,subject=sub,content=con,pic=pic,writer=request.user).save()
        else:
            messages.error(request,'빈칸없이 입력하세요')
            return redirect('gallery:create')
      
       
        return redirect('gallery:index')
    else:
     return render(request,'gallery/create.html')

def chdel(request,dpk):
    g=Gallery.objects.get(id=dpk)
    g.delete()
    return redirect('gallery:index')

def mod(request,dpk):
    g=Gallery.objects.get(id=dpk)
    if request.method == 'POST':
        sub=request.POST.get('subject')  
        pic=request.FILES.get('pic')
        con=request.POST.get('content')
        if sub:
            g.subject=sub
        if pic:
            g.pic=pic
        if con:
            g.con=con
        g.save()
        return redirect('gallery:detail',dpk=dpk)
    

    context={
        'gal':g
    }
    return render(request,'gallery/mod.html',context)

def delrep(request, gpk, dpk):
    r=Reply.objects.get(id=gpk)
    r.delete()
    return redirect('gallery:detail',dpk=dpk)

def createreply(request,dpk):
    print(request.POST)
    if request.method =='POST':
        g=Gallery.objects.get(id=dpk)
        
        rep=request.user.username
        con=request.POST.get('comment12')
        pic=request.user.pic

        
    
    

        Reply(subject=g,replyer=rep,comment=con,pic=pic).save()
    return redirect('gallery:detail',dpk=dpk)