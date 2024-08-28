from django.shortcuts import render

# Create your views here.
def conditions(request):
    d={'a':1000,'b':2000,'c':300}
    return render(request,'conditions.html',context=d)


def loop(request):
    d={'name':'lakshi','mobile': '987654321'}
    return render(request,'loop.html',context=d)
