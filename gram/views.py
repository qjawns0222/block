from django.shortcuts import redirect, render

from acc.models import User
from .models import Hashtag,Gboard
# Create your views here.
def index(request,un):
    u=User.objects.get(username=un)
    g=Gboard.objects.all()
    context={
        'gbo':g,
        'u':u
    }
    return render(request,'gram/index.html',context)

def create(request):
    if request.method == "POST":
        pic=request.POST.get('pic')
        con=request.POST.get('content')
        b=Gboard(pic=pic,content=con)
        b.save()
        for i in con.split():
            if i[0] == "#":
                h = Hashtag(name=i[1:])
                h1 = Hashtag.objects.all()
                for j in h1:
                    if j.name == i[1:]:
                        h = Hashtag.objects.get(name=i[1:])
                        break
                else:
                    h.save()
                h.hashtag.add(b)

        return redirect('gram:index')

    return render(request,'gram/create.html')
def search(request,name):
    h=Hashtag.objects.get(name=name)
    g=h.hashtag.all()
    context={
        'gbo' :g,
        'name':name
    }
    return render(request,'gram/search.html',context)