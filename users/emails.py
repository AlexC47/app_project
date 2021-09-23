from django.core.mail import send_mail, EmailMultiAlternatives
from django.shortcuts import reverse
from django.template.loader import get_template
from utils.constants import ACTIVATION_AVAILABILITY


def send_register_email(user):
    send_mail(
        subject='Your account has been registered.',
        message=f'Welcome, helper {user.first_name}.',
        from_email='alex.csibi@gmail.com',
        recipient_list=[user.email]

    )


def send_activation_email(activation):
    user = activation.user
    context = {
        'first_name': user.first_name,
        'last_name': user.last_name,
        'activation_url': f"http://localhost:8000{reverse('users:activation:activate', args=(activation.token,))}",
        'activation_value': ACTIVATION_AVAILABILITY['value'],
        'activation_unit': ACTIVATION_AVAILABILITY['unit'],
    }
    template = get_template('users/emails/activate.html')
    content = template.render(context)

    mail = EmailMultiAlternatives(
        subject='Your Account has been created',
        body=content,
        to=[user.email]
    )
    mail.content_subtype = 'html'
    mail.send()
