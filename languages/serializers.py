from rest_framework import serializers
from .models import Languages, Paradigm, Programmers


class LanguageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Languages
        fields = ['id', 'url', 'name', 'paradigm']


class ParadigmSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Paradigm
        fields = ['id', 'url', 'name']


class ProgrammersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Programmers
        fields = ['id', 'url', 'name', 'languages']
