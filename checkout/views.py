from django.shortcuts import render, reverse, redirect
from django.contrib import messages

from .forms import OrderForm
# Create your views here.


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51MMszoLzCc5HZKx6p2OGyvigfmqVhkrlavj7krS7cxtPjF5Ke7EQW7QIZZqrUB6LLjv8cmnbq4rJnuh42dPoKz8b00GUPOrT3z',  # Noqa
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
