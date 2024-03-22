from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.core.mail import send_mail

@csrf_protect
def home(request):
    if request.method == "POST":
        message_name = request.POST.get('your-name')
        message_phone = request.POST.get('your-phone')
        message_email = request.POST.get('your-email')
        message_address = request.POST.get('your-address')
        message_scheldule = request.POST.get('your-scheldule')
        message_time = request.POST.get('your-time')
        message = request.POST.get('your-message')
        # send_mail(
        #     "Apointment For: "+message_name,
        #     message,
        #     message_email,
        #     ['dremail@gmail.com'],
        #     fail_silently=False
        # )
        return render(request, 'home.html', {'message_name': message_name})
    else:
        return render(request, 'home.html', {})


@csrf_protect
def contact(request):
    message_name = None
    if request.method == "POST":
        message_name = request.POST.get('message-name')
        message_email = request.POST.get('message-email')
        message = request.POST.get('message')
        send_mail(
            "Apointment For: "+message_name,
            message,
            message_email,
            ['dremail@gmail.com'],
            fail_silently=False
        )
    return render(request, 'contact.html', {'message_name': message_name})