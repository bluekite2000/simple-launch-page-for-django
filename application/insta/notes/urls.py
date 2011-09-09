from django.conf.urls.defaults import *
from models import Note


notes = Note.objects.all()

urlpatterns = patterns(
    '',
    (r'^$','notes.views.upload_page'),

)

