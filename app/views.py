from django.shortcuts import render

# Create your views here.
def operations4(request):
    d={'a':145,'b':453,'c':124}
    return render(request,'operations4.html')