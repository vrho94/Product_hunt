from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import product
from django.utils import timezone

def home(request):
    products=product.objects.all()
    return render(request, 'products/home.html',{'products':products})

#@login_required-pomeni da za to funkcijo mora biti uporabnik vpisan da se izvede
@login_required(login_url="accounts/signup")
def create_product(request):
    if request.method=='POST':
        if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['image'] and request.FILES['icon']:
            new_product=product()
            new_product.title=request.POST['title']
            new_product.body=request.POST['body']
            new_product.url=request.POST['url']
            new_product.image=request.FILES['image']#za datoteke vedno uporabi FILES in ne POST!!!!!!!!!!!!!!1
            new_product.icon=request.FILES['icon']
            new_product.pub_date=timezone.datetime.now()# import timezone... glej gor
            new_product.hunter=request.user
            new_product.save()
            return redirect('/products/'+str(new_product.id))
        else:
                return render(request, 'products/create.html', {'error':'All fileds are required'})
    else:
        return render(request, 'products/create.html')

def detail(request, product_id):
    show_product = get_object_or_404(product, pk=product_id)
    return render(request, 'products/detail.html',{'product':show_product})

@login_required(login_url="/accounts/signup")
def upvote(request,product_id):
    if request.method=='POST':
        show_product = get_object_or_404(product, pk=product_id)
        show_product.votes_total +=1
        show_product.save()
        return redirect('/products/'+str(show_product.id))
