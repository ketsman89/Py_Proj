from typing import Any, Optional
from django.db import models
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from django.views.generic import DetailView

from . import models
from spravochniki.models import Book


# Create your views here.

class CartDetailView(DetailView):
    template_name = "orders/cart.html"
    model = models.Cart

    def get_object(self, *args, **kwargs):
        print(self.request.GET.get("good_id"))
        print(self.request.GET.get("quantity"))
        cart_pk = self.request.session.get("cart_id")
        customer = self.request.user
        if customer.is_anonymous:
            customer = None
        cart, created = models.Cart.objects.get_or_create(
            pk=cart_pk,
            defaults={
                "customer": customer
            }
        )
        good_id = self.request.GET.get("good_id")
        quantity=self.request.GET.get("quantity")
        
        if good_id and quantity:
            quantity = int(quantity)
            good = Book.objects.get(pk=int(good_id))       
            price = good.price
            good_in_cart, good_in_cart_created = models.GoodInCart.objects.get_or_create(
                cart=cart,
                good=good,
                defaults={
                    "quantity":quantity,
                    "price":price * quantity,
                }            
            )
            if not good_in_cart_created:
                good_in_cart.quantity = good_in_cart.quantity + quantity
                good_in_cart.price = good_in_cart.price + price * quantity
                good_in_cart.save()
            if created:
                self.request.session['cart_id'] = cart.pk
        print(cart)
        return cart
    
class CartAddDeleteItemView(DetailView):
    template_name = "orders/cart.html"
    model = models.Cart

    def get_object(self, *args, **kwargs):       
        cart_pk = self.request.session.get("cart_id")
        customer = self.request.user
        if customer.is_anonymous:
            customer = None
        cart, created = models.Cart.objects.get_or_create(
            pk=cart_pk,
            defaults={
                "customer": customer
            }
        )
        good_id = self.request.GET.get("good")
        action=self.request.GET.get("action")
        
        if good_id and action and action in ['add', 'delete']:
            
            good = Book.objects.get(pk=int(good_id))       
            price = good.price
            good_in_cart = get_object_or_404(
                models.GoodInCart,
                cart=cart,
                good=good,                            
            )         
            if action == "add":
                addition = 1
            else:
                addition = -1
                good_in_cart.quantity = good_in_cart.quantity + addition
                good_in_cart.price = good_in_cart.quantity * price
                good_in_cart.save()
        return cart