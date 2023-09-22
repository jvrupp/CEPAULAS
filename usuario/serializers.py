from rest_framework import serializers
from .models import Usuario
from valida_cep.models import Enderecos
import requests

def consulta_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    
    try:
        response = requests.get(url)
        data = response.json()
        print(data)
    except Exception as e:
        print("Ocorreu um erro ao consultar o CEP:", str(e))

class RegistroSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)
    class Meta:
        model = Usuario
        fields = ('id', 'username', 'email','password','password2','cep')
        extra_kwargs = {'password': {'write_only': True},'password2': {'write_only': True}}
    def create(self, validated_data):
        password = validated_data.pop('password')
        password2 = validated_data.pop('password2')
        cep = validated_data.pop('cep')
        consulta_cep(cep)
        if password == password2 and password is not None:
            instance = Usuario(**validated_data)
            instance.set_password(password)
            instance.save()
        else:
            raise serializers.ValidationError("{'resp':'As senhas não coincidem'}")

        return instance