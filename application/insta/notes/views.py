
from django.middleware.csrf import  get_token
from django.conf import settings
from forms import WaitList
from django.shortcuts import redirect, render	
from django.core.mail import mail_admins




def contact_form(request):
    fileObj = open(settings.MEDIA_ROOT+'/'+'phone.txt',"a")
    if request.POST:
        form = WaitList(request.POST)
        if form.is_valid():
            message = " Email:%s\r\n" % (
                form.cleaned_data['My_email_is'],			
             
            )

            fileObj.write(form.cleaned_data['My_email_is']+'\n')

            fileObj.close()
            mail_admins('Contact form', message, fail_silently=False)
            if request.is_ajax():
                return render(request, 'thanks.html')
            else:
                return redirect('thanks')
    else:
        form = WaitList()

    return render(request, 'index.html', {'form':form})