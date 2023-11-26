from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import CustomUserCreationForm  # Importe o novo formulário

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = CustomUserCreationForm()

    context = {'form': form}
    return render(request, 'accounts/signup.html',context)