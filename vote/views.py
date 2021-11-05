from typing import ContextManager
from django.shortcuts import redirect, render
from django.contrib import messages
from django.core.paginator import Paginator
from django.utils import timezone
from vote.models import Topic,Choice,Reply

# Create your views here.
def index(request):
    kw=request.GET.get('kw','')
    cate=request.GET.get('cate','con')
    if kw:
        if cate == 'top':
            t=Topic.objects.filter(subject__contains = kw)
        elif cate == 'con':
            t=Topic.objects.filter(content__contains = kw)
        elif cate == 'sel':
            t=Choice.objects.filter(select__contains = kw)
        else :
            t=Topic.objects.filter(writer__startswith    = kw)
    else:
         t=Topic.objects.all().order_by("-ctime")
    page=request.GET.get('page',1)
    pag=Paginator(t,3)
    obj=pag.get_page(page)
    context={
        'top':obj,
        'kw':kw,
        'cate':cate
    }
    return render(request,'vote/index.html',context)

def detail(request,dpk):
    t=Topic.objects.get(id=dpk)
    r=t.reply_set.all()
    c=t.choice_set.all()
    page=request.GET.get('page',1)
    pag=Paginator(r,5)
    obj=pag.get_page(page)
    context={
        'top':t,
        'cho':c,
        'rep':obj,
        
    }
    return render(request,'vote/detail.html',context)

def vote(request,tpk):

    t=Topic.objects.get(id=tpk)
    if not request.user in t.voter.all():
        s=request.POST.get("select")
        if not s:
            messages.error(request,'한개이상 선택하세요')
            return redirect("vote:detail",dpk=tpk)
        else:
            t.voter.add(request.user)
            
            c=Choice.objects.get(id=s)
            c.voter.add(request.user)
    return redirect("vote:detail",dpk=tpk)
    

def cancel(request,cpk):
    t=Topic.objects.get(id=cpk)
    t.voter.remove(request.user)
    c = t.choice_set.all()
   
    for i in c:
        if request.user in i.voter.all():
            i.voter.remove(request.user)
    return redirect('vote:detail',dpk=cpk)

def create(request):
    if request.method == "POST":
        top=request.POST.get("topic")
        wri=request.user.username
        con=request.POST.get("content")
        t=Topic(subject=top,writer=wri,ctime=timezone.now(),content=con)
        t.save()
        sels = request.POST.getlist("select")
        coms = request.POST.getlist("comment")
        pics = request.FILES.getlist("pic")

        for i,j,k in zip(sels,coms,pics):
            Choice(subject=t,select=i,comment=j,pic=k).save()
        return redirect('vote:index')
    return render(request,'vote/create.html')

def delrep(request,dpk,tpk):
   
    r= Reply.objects.get(id=dpk)
    r.delete()
    return redirect('vote:detail',dpk=tpk)

def createreply(request,dpk):
    
    if request.method == 'POST':
        t=Topic.objects.get(id=dpk)
        rep=request.user.username
        com=request.POST.get("comment12")
        pic=request.user.pic
        Reply(sub=t,replyer=rep,comment=com,pic=pic).save()
        return redirect('vote:detail',dpk=dpk)