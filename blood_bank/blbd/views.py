from django.shortcuts import render
from .models import donor
from .models import receiver
from .models import stocks
# Create your views here.
def home(request):
    return render(request,'home.html')

def receivers(request):
    receive = receiver.objects.all()
    print(receive)
    nrows = len(receive)
    params = {"no._of_rows":nrows,"range":range(nrows),"receiver":receive}
    return render(request,'receivers.html',params)

def donors(request):
    donate = donor.objects.all()
    print(donate)
    nrows = len(donate)
    params = {"no._of_rows": nrows, "range": range(nrows), "donor": donate}
    return render(request, 'donors.html',params)

def workers(request):
    return render(request,'workers.html')

def stock(request):
    vol = stocks.objects.all()
    Apos = stocks.A_positive
    Aneg = stocks.A_negative
    Bneg = stocks.B_negative
    Bpos = stocks.B_positive
    Oneg = stocks.O_negative
    Opos = stocks.O_positive
    ABpos = stocks.AB_positive
    ABneg = stocks.AB_negative
    params = {"Apos":Apos , "Aneg":Aneg , "Bpos":Bpos , "Bneg":Bneg , "vol":vol}
    return render(request,'stock.html',params)

def myths(request):
    return render(request,'myth.html')

def who(request):
    return render(request,'WHO.html')