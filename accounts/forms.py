from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Empresa

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class EmpresaSignUpForm(forms.ModelForm):
    # Campos específicos para a Empresa
    cnpj = forms.CharField(label='CNPJ')
    nome_fantasia = forms.CharField(label='Nome Fantasia')
    endereco = forms.CharField(label='Endereço')
    telefone = forms.CharField(label='Telefone')

    # Campos de usuário, se necessário
    username = forms.CharField(label='Username')
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = Empresa
        fields = ['cnpj', 'nome_fantasia', 'endereco', 'telefone']

    def save(self, commit=True):
        empresa = super().save(commit=False)
        empresa.cnpj = self.cleaned_data['cnpj']
        empresa.nome_fantasia = self.cleaned_data['nome_fantasia']
        empresa.endereco = self.cleaned_data['endereco']
        empresa.telefone = self.cleaned_data['telefone']
        
        if commit:
            empresa.save()
        
        return empresa
