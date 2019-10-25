from rest_framework import serializers
from .models import Languages


class LanguageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Languages
        fields = ['id', 'url', 'name', 'paradigm']
