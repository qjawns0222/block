from typing import ContextManager
from django.shortcuts import render,redirect

# Create your views here.
import pdfplumber
def plum_daldal(filename):
    with pdfplumber.open(filename) as pdf:
        b=''
        for i in range(len(pdf.pages)):
            page = pdf.pages[i]
            b+=page.extract_text()

def index(request):
    import pdfplumber
    b=''
    c=request.FILES.get('pic')
    
    
    if c:
        with pdfplumber.open(c) as pdf:
            
            for i in range(len(pdf.pages)):
                page = pdf.pages[i]
                b+=page.extract_text()
    

    context={
        'ca' : c,
        'b' : b
    }
    
    return render(request,'tract/index.html',context)


