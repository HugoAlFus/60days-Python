from django.shortcuts import render, redirect, get_object_or_404

from .forms import AddToCartForm
from .models import Product


def product_list(request):
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products})


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = AddToCartForm()
    return render(request, 'store/product_detail.html', {'product': product, 'form': form})


def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = AddToCartForm(request.POST)
    if form.is_valid():
        cart = request.session.get('cart', {})
        cart[str(pk)] = cart.get(str(pk), 0) + form.cleaned_data['quantity']
        request.session['cart'] = cart
    return redirect('cart_detail')


def cart_detail(request):
    cart = request.session.get('cart', {})
    items = []
    total = 0
    for pk, quantity in cart.items():
        product = Product.objects.get(pk=pk)
        subtotal = product.price * quantity
        items.append({'product': product, 'quantity': quantity, 'subtotal': subtotal})
        total += subtotal
    return render(request, 'store/cart_detail.html', {'items': items, 'total': total})


def checkout(request):
    request.session['cart'] = {}  # Vaciar carrito
    return render(request, 'store/checkout.html')
