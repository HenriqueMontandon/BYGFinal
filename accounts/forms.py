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
    username = forms.CharField(label='Username')
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = Empresa
        fields = ['username', 'email', 'cnpj', 'nome_fantasia', 'endereco', 'telefone']

    def save(self, commit=True):
        empresa = super().save(commit=False)
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password']
        )
        empresa.user = user
        
        if commit:
            user.save()
            empresa.save()
        
        return empresa