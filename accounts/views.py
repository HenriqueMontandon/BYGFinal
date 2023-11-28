from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import CustomUserCreationForm, EmpresaSignUpForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, Group, Permission
from django.db import IntegrityError

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

from django.contrib.auth.models import Group

from django.contrib.auth.models import Group

def empresa_signup(request):
    if request.method == 'POST':
        form = EmpresaSignUpForm(request.POST)
        if form.is_valid():
            # Salvando os dados da empresa
            empresa = form.save(commit=False)
            empresa.save()

            # Criando um usuário associado à empresa
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # Criação do usuário Django
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )

            # Adicionando o usuário ao grupo de empresas
            group = Group.objects.get(name='empresas_users')
            user.groups.add(group)

            # Associando o usuário criado à empresa
            empresa.user = user
            empresa.save()

            return HttpResponseRedirect(reverse('index'))
    else:
        form = EmpresaSignUpForm()

    return render(request, 'accounts/empresa_signup.html', {'form': form})

