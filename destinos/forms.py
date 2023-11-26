from django.forms import ModelForm
from .models import Destino, Review, List
from .models import PreferenciaTipo, Preferencia
from django import forms

class DestinoForm(ModelForm):
    class Meta:
        model = Destino
        fields = [
            'name',
            'categoria',
            'descricao',
            'destino_url',
        ]
class RoteiroForm(ModelForm):
    class Meta:
        model = List
        fields = [
            'Nome',
            'Capa',
            'autor',
            'atracoes'
        ]
    
class ReviewRoteiroForm(ModelForm):
    class Meta:
        model = Review
        fields = [
            'text',
        ]
        labels = {
            'text': 'Resenha',
        }

class PreferenciaTipoForm(ModelForm):
    class Meta:
        model = PreferenciaTipo
        fields = ['nome']  # Campos do formulário para adicionar preferência tipo

class PreferenciaForm(forms.ModelForm):
    class Meta:
        model = Preferencia
        fields = ['preferencia_tipo', 'nota']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nota'].widget = forms.NumberInput(attrs={'min': '1', 'max': '10', 'placeholder': 'Atribua uma nota (1-10)'})
