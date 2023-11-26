from django.forms import ModelForm
from .models import Destino, Review, List
from .models import PreferenciaTipo

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