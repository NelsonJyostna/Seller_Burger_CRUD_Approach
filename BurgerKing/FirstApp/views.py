from django.shortcuts import render, redirect
from .models import Seller
from .forms import SellerForm
from django.http import HttpResponse




# Create your views here.
# def loginSellerView(request):
#     form=SellerForm()
#     if request.method=='POST':
#         form=SellerForm(request.POST)
#         if form.is_valid():

def home(request):
    template_name='FirstApp/home.html'
    context={}
    return render(request, template_name, context)

def addSellerView(request):
   form=SellerForm()
   if request.method=='POST':
       print("Nelson")
       form=SellerForm(request.POST, request.FILES)
       if form.is_valid():
            # um = form.cleaned_data['uname']
            # mo = form.cleaned_data['mobno']
            # el = form.cleaned_data['email']
            # bt = form.cleaned_data['burg_type']
            # bi=  form.cleaned_data['burg_image']
            # gr = form.cleaned_data['gender']
            # od = form.cleaned_data['order_date']
            # u1=Seller(uname=um, mobno=mo, email=el, burg_type=bt, burg_image=bi , gender=gr, order_date=od )
            form.save()
            # u1.save()
            return redirect('showseller')
   template_name='FirstApp/addseller.html'
   context={'form':form}
   return render(request, template_name, context)


def showSellerView(request):
    prods=Seller.objects.all()
    context={'prods':prods}
    template_name='FirstApp/showseller.html'
    return render(request, template_name, context)


def updateSellerView(request, id):
    sell_obj=Seller.objects.get(id=id)
    print('Nelson')
    form=SellerForm(instance=sell_obj)
    print("Nelson21354354")
    if request.method=='POST':
        print("Post Method")
        form=SellerForm(request.POST, instance=sell_obj)
        if form.is_valid():
            form.save()
            return redirect('showseller')
    template_name = 'FirstApp/addseller.html'
    context = {'form': form}
    return render(request, template_name, context)


def deleteSellerView(request, id):
    sell_obj=Seller.objects.get(id=id)
    sell_obj.delete()
    return redirect('showseller')





