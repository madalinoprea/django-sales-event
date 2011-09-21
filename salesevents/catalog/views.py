# Create your views here.

from mario.utils import render_to
from catalog.models import Event, Product

from datetime import datetime, timedelta
from django.shortcuts import get_object_or_404

@render_to('home.html')
def home(request):
    return {
        'open_events': Event.open_events.all(),
        'upcoming_events': Event.upcoming_events.all(),
        'closed_events': Event.closed_events.filter(end_date__gte=datetime.now() - timedelta(days=2))}

@render_to('event.html')    
def event(request, event_id):
    event = get_object_or_404(Event.open_events, pk=event_id)
    
    # Sorting options FIXME: Validate that only allowed orders
    order_by = request.GET.get('order_by', 'name')
    order_dir = request.GET.get('dir', 'asc')
    if order_dir == 'desc':
        order_by = '-%s' % order_by
    
    
    products = event.get_products()
    products = products.order_by(order_by)
    #TODO: Add order by
    return {'event': event, 'products': products}

@render_to('product.html')
def product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return {'product': product}


