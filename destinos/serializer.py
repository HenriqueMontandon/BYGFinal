from rest_framework import serializers
from .models import Destino

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model=Destino
        fields=('name','destino_url','descricao','coordenadas','preco','categoria','empresaid')