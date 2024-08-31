from django.shortcuts import redirect, render
from django.core.mail import send_mail
from django.conf import settings
from .models import blog  # Adjust the import based on your actual model name

def home(request):
    data = blog.objects.all()
    if data:
        return redirect('admin/')
    context = {'data': data}
    if request.method == 'POST':
        # Extract form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        reason = request.POST.get('reason')
        message_content = request.POST.get('message')
        subject = f'Application regarding{reason}'
        message_body = f'Dear Sir/Madam,\n\n{message_content}'
        sender = email
        receiver = settings.EMAIL_HOST_USER
        print(email)
        send_mail(
                subject,
                message_body,
                sender,
                [receiver],
            )
        print('Email sent successfully')
    return render(request, 'home.html', context)
