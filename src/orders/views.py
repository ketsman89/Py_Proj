from typing import Any, Optional
from django.db import models
from django.shortcuts import render

from django.views.generic import DetailView

from . import models

# Create your views here.

class CartDetailView(DetailView):
    template_name = "orders/cart.html"
    model = models.Cart

    def get_object(self, *args, **kwargs):
        print(self.request.GET.get("good_id"))
        print(self.request.GET.get("quantity"))
        pk = self.request.session.get("cart_id")
        customer = self.request.user
        if customer.is_anonymous:
            customer = None
        cart, created = models.Cart.objects.get_or_create(
            pk=pk,
            defaults={
                "customer": customer
            }
        )
        if created:
            self.request.session['cart_id'] = cart.pk
        return cart