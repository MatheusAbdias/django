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
                {"cpf": "O CPF deve ter 11 dígitos "}
            )
        return data
    #     if len(cpf) != 11:
    #         raise serializers.ValidationError("O cpf deve ter 11 digitos")
    #     return cpf
    # def validate_name(self,name):
    #     if not name.isapha():
    #         raise serializers.ValidationError("Não inclua números neste campo")
    #     return name
    # def validate_rg(self, rg):
    #     if len(rg) != 9:
    #         raise serializers.ValidationError("O RG deve ter 9 diigitos")
    #     return rg
    # def validate_celular(self,celular):
    #     if len(celular) < 11:
    #         raise serializers.ValidationError("O celular deve ter 11 digitos")
    #     return celular