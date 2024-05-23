from django.shortcuts import render
from .tasks import send_mail
# Create your views here.



def send_mails(request):
    #call celery task
    send_mail.delay()
    return render(request, '')
