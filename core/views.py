from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .models import blog  # Adjust the import based on your actual model name

def home(request):
    data = blog.objects.all()
    context = {'data': data}

    if request.method == 'POST':
        # Extract form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        reason = request.POST.get('reason')
        message_content = request.POST.get('message')
        subject = f'Application regarding {reason}'
        message_body = f'Dear Sir/Madam,\n\n{message_content}'
        sender = settings.EMAIL_HOST_USER
        receiver = email
        
        # Debugging: Print the extracted values
        print('Received POST request')
        print('Name:', name)
        print('Email:', email)
        print('Phone:', phone)
        print('Reason:', reason)
        print('Message Content:', message_content)
        print('Subject:', subject)
        print('Message Body:', message_body)
        print('Sender:', sender)
        print('Receiver:', receiver)
        send_mail(
                subject,
                message_body,
                sender,
                [receiver],
            )
        print('Email sent successfully')
    return render(request, 'home.html', context)
