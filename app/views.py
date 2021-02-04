from django.shortcuts import render
from app.models import From2
# Create your views here.
def from2(request):
    if request.method=="POST":
        first=request.POST.get('first')
        last=request.POST.get('last')
        father_name=request.POST.get('father_name')
        mother_name=request.POST.get('mather_name')
        email=request.POST.get('email')
        address=request.POST.get('address')
        city=request.POST.get('city')
        number=request.POST.get('number')
        number1=request.POST.get('number1')
        
        #Aadhrnumber=request.POST.get('Aadhrnumber')
        f=From2.objects.get_or_create(first=first,last=last,father_name=father_name,mother_name=mother_name,email=email,address=address,city=city,number=number,number1=number1)[0]
        f.save()
    return render(request,'from2.html')