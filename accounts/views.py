from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import CustomUserCreationForm

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            send_welcome_email(user.email)  # Envie o e-mail de boas-vindas
            return HttpResponseRedirect(reverse('index'))
    else:
        form = CustomUserCreationForm()

    context = {'form': form}
    return render(request, 'accounts/signup.html', context)

def send_welcome_email(user_email):
    subject = 'Bem-vindo à BYG!'
    message = (
        'Parabéns, você se cadastrou no nosso site. '
        'Agora você vai poder desfrutar do melhor que a BYG pode oferecer. '
        'Venha viajar conosco.'
    )
    from_email = 'bygsiteoficial@outlook.com'  # Seu endereço de e-mail
    send_mail(subject, message, from_email,[user_email])