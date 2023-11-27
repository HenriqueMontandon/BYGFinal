# accounts/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Empresa

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1','password2']

class EmpresaSignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Empresa
        fields = ['username', 'email', 'password', 'cnpj', 'nome_fantasia', 'endereco', 'telefone']

    def save(self, commit=True):
        empresa = super().save(commit=False)
        username = f'empresa_{self.cleaned_data["username"]}'  # Adicione um prefixo único
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        user = User.objects.create_user(username=username, email=email, password=password)
        empresa.user_ptr = user
        if commit:
            empresa.save()
        return empresa
