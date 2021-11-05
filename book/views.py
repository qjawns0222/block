from django.shortcuts import render,redirect
from .models import Book
from django.utils import timezone
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    page=request.GET.get('page',1)
    b=request.user.book_set.all()
    pag=Paginator(b,6)
    obj=pag.get_page(page)
    context={
        'blist':obj
    }
    return render(request,"book/index.html",context)

def create(request):
    if request.method == "POST":
        ck = request.POST.get("ck")
        surl = request.POST.get("surl")
        sname = request.POST.get("sname")
        if ck:
           impo = True
        else:
            impo=False
        Book(user=request.user,site_name=sname, site_url=surl, impo=impo,cttime=timezone.now()).save()
        return redirect("book:index")
    return render(request, "book/create.html")

def linkdel(request,bpk):
    b=Book.objects.get(id=bpk)
    b.delete()
    return redirect('book:index')
