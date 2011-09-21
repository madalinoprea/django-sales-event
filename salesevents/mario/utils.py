'''
Created on Aug 13, 2010

@author: mario
'''

from django.http import HttpResponse
from django.utils import simplejson
from django.core.mail import mail_admins
from django.utils.translation import ugettext as _
import sys
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.db.models.expressions import ExpressionNode
import urllib


def render_json(func):
    '''
    Use this decorator on a function that returns a dict to get a JSON view, with error handling.

    Features:
        response always includes a 'result' attribute ('ok' by default)
        catches all errors and mails the admins
        always returns JSON even on errors
    @param func: view
    '''
    def wrap(request, *a, **kw):
        response = None
        try:
            response = func(request, *a, **kw)
            assert isinstance(response, dict)
            if 'result' not in response:
                response['result'] = 'ok'
        except KeyboardInterrupt:
            # Allow keyboard interrupts through for debugging.
            raise
        except Exception, e:
            # Mail the admins with the error
            exc_info = sys.exc_info()
            subject = 'JSON view error: %s' % request.path
            try:
                request_repr = repr(request)
            except:
                request_repr = 'Request repr() unavailable'
            import traceback
            message = 'Traceback:\n%s\n\nRequest:\n%s' % (
                '\n'.join(traceback.format_exception(*exc_info)),
                request_repr,
                )
            mail_admins(subject, message, fail_silently=True)

            # Come what may, we're returning JSON.
            if hasattr(e, 'message'):
                msg = e.message
            else:
                msg = _('Internal error')+': '+str(e)
            response = {'result': 'error',
                        'text': msg}

        json = simplejson.dumps(response)
        return HttpResponse(json, mimetype='application/json')
    return wrap


def render_to( template_name):
    '''
    Use this to decorate a view to specify the template to be used.

    @param template_name:
    '''
    def renderer(func):
        def wrapper(request, *args, **kw):
            output = func(request, *args, **kw)
            if not isinstance(output, dict):
                return output
            return render_to_response(template_name, output, RequestContext(request))
        return wrapper
        wrapper.__name__ = func.__name
        wrapper.__doc__ = func.__doc__
    return renderer

def download(url, path):
    web_file = urllib.urlopen(url)
    filename = url.split('/')[-1]
    local_file = open('%s/%s' % (path, filename), 'w')
    local_file.write( web_file.read() )
    web_file.close()
    local_file.close()
    
    return filename

# Atomic updates from disqus: FIXME Not tested
def update(self, using=None, **kwargs):
    '''
    Updates specified attributes on the current instance
    @param using:
    '''
    assert self.pk, "Cannot update on instance that has not yet been created."
    
    self.__class__.base_manager.using(using).filter(pk=self.pk).update(*kwargs)
    for k, v in kwargs.iteritems():
        if isinstance(v, ExpressionNode):
            # NotImplemented
            continue
        setattr(self, k, v)
update.alters_data = True
    