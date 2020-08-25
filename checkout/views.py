from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your cart at the moment")
        return redirect(reverse('commissions'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51HHQu4LMfxDapyn5gCJfdDe2r7gChHX0tZvH8oU5hFJrgPXQ1Zlq4pedoPIP2T9XmTfPJ8D0lZiz76rJ6uybR9gr00DXbVNjwq',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
