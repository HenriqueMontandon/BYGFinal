from django.forms import ModelForm
from .models import Destino, Review, List, Evento, Categoria
from .models import PreferenciaTipo, Preferencia
from django import forms
from .models import AtracaoCaracteristica

class DestinoForm(ModelForm):
    class Meta:
        model = Destino
        fields = [
            'name',
            'categoria',
            'descricao',
            'destino_url',
            'empresaid',
            'coordenadas',
            'preco',
        ]

class RoteiroForm(ModelForm):
    class Meta:
        model = List
        fields = [
            'nome',
            'Capa',
            'descricao',
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


class AtracaoCaracteristicaForm(forms.ModelForm):
    class Meta:
        model = AtracaoCaracteristica
        fields = ['caracteristica_tipo','nota']  # Campos do formulário para adicionar características de atração

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nota'].widget = forms.NumberInput(attrs={'min': '1', 'max': '10', 'placeholder': 'Atribua uma nota (1-10)'})  # Personalização do widget para o campo 'nome'

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['destino_id', 'data_inicio', 'data_fim']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['data_inicio'].widget.attrs.update({'class': 'datepicker'})
        self.fields['data_fim'].widget.attrs.update({'class': 'datepicker'})

    def clean(self):
        cleaned_data = super().clean()
        data_inicio = cleaned_data.get('data_inicio')
        data_fim = cleaned_data.get('data_fim')

        if data_inicio and data_fim and data_inicio > data_fim:
            raise forms.ValidationError('A data de início não pode ser posterior à data de término.')

        return cleaned_data

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['name']