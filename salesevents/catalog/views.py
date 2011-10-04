# Create your views here.

from mario.utils import render_to
from catalog.models import Event, Product, Category

from datetime import datetime, timedelta
from django.contrib.auth import logout
from django.contrib.auth.views import redirect_to_login
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

@login_required
@render_to('home.html')
def home_view(request):
    return {
        'open_events': Event.open_events.all(),
        'upcoming_events': Event.upcoming_events.all(),
        'closed_events': Event.closed_events.filter(end_date__gte=datetime.now() - timedelta(days=2))
    }


@render_to('event.html')    
def event_view(request, event_slug):
    event = get_object_or_404(Event.open_events, slug=event_slug)
    
    # Sorting options TODO: Validate that only allowed orders
    order_by = request.GET.get('order_by', 'name')
    order_dir = request.GET.get('dir', 'asc')
    if order_dir == 'desc':
        order_by = '-%s' % order_by
    
    
    products = event.get_products()
    products = products.order_by(order_by)
    #TODO: Add order by
    return {'event': event, 'products': products}

@render_to('event.html')
def event_category_view(request, event_slug, category_slug):
    event = get_object_or_404(Event.open_events, slug=event_slug)
    # TODO: check if category is under this event
    category = get_object_or_404(Category, slug=category_slug)
    products = category.get_products()

    return {'event': event, 'category': category, 'products': products}

@render_to('product.html')
def event_product_view(request, event_slug, category_slug):
    event = get_object_or_404(Event.open_events, slug=event_slug)
    products = event.category.get_products()
    print type(products)
    
    return {}

@render_to('product.html')
def product_view(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return {'product': product}

def logout_view(request):
    logout(request)

    return redirect_to_login(reverse('home'))

def signup_view(request):
    pass
