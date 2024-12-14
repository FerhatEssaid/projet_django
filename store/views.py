from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from store.models import product ,order , cart

def index(request) :
    products=product.objects.all()
  
    return render(request,'store/index.html',context={"products":products})
    

def product_detail(request,slug):
     products = get_object_or_404(product,slug=slug)
     return render (request,'store/detail.html',context={"products":products})


def add_to_cart(request,slug):
     user=request.user
     products = get_object_or_404(product,slug=slug)
     Cart, _ =cart.objects.get_or_create(user=user)
     Order,created =order.objects.get_or_create(user=user,product=products)
     if created :
          Cart.orders.add(Order)
          Cart.save()
     else:
          Order.quantity +=1
          Order.save()

     return redirect (reverse("product", kwargs={"slug": slug}))

def carte(request):
    # Récupérer le panier de l'utilisateur connecté
    carts = get_object_or_404(cart, user=request.user)
    
    # Passer les commandes associées au panier au template
    return render(request, 'store/carte.html', context={"orders": carts.orders.all()})
def delete_carte(request):
     #  cart =request.user.cart 
     #  if cart
     if cart :=request.user.cart :
          cart.orders.all().delete()
          cart.delete()
     return redirect ('index')     

