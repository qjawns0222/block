from django.shortcuts import redirect, render
import googletrans
from googletrans import Translator
 

# Create your views here.
def index(request):
   
    cate = request.GET.get('cate','')
    cate1 = request.GET.get('cate1','en')
    text1 = request.GET.get('text1','')
    text2 = request.GET.get('text2','')
    if text1:
        translator=Translator() 
        trans = translator.translate(text1, src=cate, dest=cate1)
        text2=trans.text
    context={
        'cate':cate,
        'cate1':cate1,
        'text1':text1,
        'text2':text2,
    }
    return render(request,'trans/index.html',context)

