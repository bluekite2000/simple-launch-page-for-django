from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from notes.views import *



urlpatterns = patterns('notes.views',
    url(r'^$', 'contact_form', name="contact_form"),
    url(r'^thanks/$', direct_to_template, {'template': 'thanks.html'},name="thanks"),


)

