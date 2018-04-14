# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

def index(request):
    if "itemcount" not in request.session:
        request.session["itemcount"] = 0
    if "total" not in request.session:
        request.session["total"] = 0
    return render(request, "index.html")

def buy(request):
    d ={"1" : 20, "2" : 30, "3" : 5, "4" : 50}
    if request.method == "POST":
        qty = request.POST["quantity"]
        request.session["itemcount"] += int(qty)
        priceid = request.POST["price"]
        price = d[priceid] 
        request.session["price"] = price
        request.session["total"] += price        
        
    return redirect("/amadon/checkout")

def checkout(request):
    return render(request, "checkout.html")

def clear(request):
    request.session.flush()
    return redirect('/amadon/checkout')