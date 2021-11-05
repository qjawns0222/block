from django.shortcuts import render
import pytesseract
from PIL import Image
from googletrans import Translator

# Create your views here.
def index(request):
    b=''
    cate=''
    if request.method =='POST':
        cate = request.POST.get('cate','')
        c=request.FILES.get('pic')
        pytesseract.pytesseract.tesseract_cmd = 'tes/tesseract.exe'
        img = Image.open(c)
        text = pytesseract.image_to_string(img, lang=cate)
        b=text
        
        
        
        
    context={
        'b':b,
        'cate':cate

    }
        
    return render(request,'tesr/index.html',context)


def trans(request):
    b=request.POST.get('d')
    cate = request.GET.get('cate','')
    cate1 = request.GET.get('cate1','en')
    text1 = request.GET.get('text1','b')
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
    return render(request,'tesr/trans.html',context)
