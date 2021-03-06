from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Cliente


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nome', 'endereco', 'idade']
        #fields = ('id', 'nome', 'endereco', 'idade')
