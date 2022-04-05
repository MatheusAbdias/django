from re import search
from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import * 
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
    
    def validate(self,data):
        if not validete_cpf(data["cpf"]):
            raise serializers.ValidationError(
                {"cpf": "CPF invalido "}
            )
        if not validate_nome(data["nome"]):
            raise  serializers.ValidationError(
                {"nome":"Não inclua digitos neste campo"}
            )
        if not validate_rg(data["rg"]):
            raise serializers.ValidationError(
                {"rg":"O RG deve ter 9 dígitos"}
            )
        if validate_celular(data["celular"]):
            raise serializers.ValidationError(
                {"celular":"O número de celular deve serguir este mode:11 91234-1234"}
                )
        return data