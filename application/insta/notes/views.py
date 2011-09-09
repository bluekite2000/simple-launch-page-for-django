from django.utils import simplejson
from models import Note
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseServerError
from django.middleware.csrf import  get_token
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.conf import settings
	


def upload_page(request):
	ctx=RequestContext(request,{
	'csrf_token':get_token(request),
	})	
	return render_to_response( 'index.html', ctx )
