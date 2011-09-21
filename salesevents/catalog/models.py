from django.db import models
from django.utils.translation import ugettext as _

from mptt.models import MPTTModel
from datetime import datetime

class Category(MPTTModel):
    """Category of products"""
    name = models.CharField(max_length=32)
    parent = models.ForeignKey('self', related_name='children', null=True, blank=True)
    
    class Meta:
        verbose_name_plural = 'Categories'
    
    def __unicode__(self):
        return self.name
    
    def delete(self):
        super(Category, self).delete()
        
    
    # @models.permalink
    # def get_absolute_url(self):
    #     return ('view_or_url_name' )
    
class OpenEventsManager(models.Manager):
    def get_query_set(self):
        now = datetime.now()
        return super(OpenEventsManager, self).get_query_set().filter(
                                                        enabled=True, 
                                                        start_date__lte=now, 
                                                        end_date__gte=now)
    
class ClosedEventsManager(models.Manager):
    def get_query_set(self):
        return super(ClosedEventsManager, self).get_query_set().filter(
                                                        enabled=True, 
                                                        end_date__lte=datetime.now())
    
class UpcomingEventsManager(models.Manager):
    def get_query_set(self):
        now = datetime.now()
        return super(UpcomingEventsManager, self).get_query_set().filter(
                                                        enabled=True, 
                                                        start_date__gte=now,
                                                        end_date__gte=now)

EVENT_STATUS_OPEN = 0
EVENT_STATUS_UPCOMING = 1
EVENT_STATUS_CLOSED = 2

EVENT_STATUS_TEXT = {
    EVENT_STATUS_OPEN: _('Open'),
    EVENT_STATUS_UPCOMING: _('Upcoming'),
    EVENT_STATUS_CLOSED: _('Closed')
}

class Event(models.Model):
    
    """Sales Event"""
    name = models.CharField(max_length=32)
    category = models.ForeignKey(Category)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    enabled = models.BooleanField(default=True)
    sort_order = models.IntegerField(default=0)
    
    objects = models.Manager()
    open_events = OpenEventsManager()
    closed_events = ClosedEventsManager()
    upcoming_events = UpcomingEventsManager()
    
    def __unicode__(self):
        return self.category.name
    
    def is_open(self):
        return self.start_date < datetime.now() and self.end_date > datetime.now()
    
    def is_closed(self):
        return (not self.is_open())
    
    def status(self):
        now = datetime.now()
        if self.start_date < now < self.end_date:
            return EVENT_STATUS_OPEN
        elif self.end_date < now:
            return EVENT_STATUS_CLOSED
        elif self.start_date > now:
            return EVENT_STATUS_UPCOMING
    
    def status_text(self):
        return EVENT_STATUS_TEXT[self.status()]
    
    def get_products(self):
        return Product.objects.filter(categories__in=self.category.get_descendants()).distinct()
    
    
    # FIXME: Check if start_date is < end_date when saving model
    
    @models.permalink
    def get_absolute_url(self):
        return ('event', (self.pk,))


class Product(models.Model):
    """ Product model """
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=256)
    short_description = models.CharField(max_length=128)
    sku = models.CharField(max_length=24)
    status = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=19, decimal_places=4)
    categories = models.ManyToManyField(Category, related_name='products')

    def __unicode__(self):
        return self.name
    
    @models.permalink
    def get_absolute_url(self):
        return ('product', (self.pk,))
