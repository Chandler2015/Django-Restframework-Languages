from django.shortcuts import render
from rest_framework import viewsets
from .models import Languages, Paradigm, Programmers
from .serializers import LanguageSerializer, ParadigmSerializer, ProgrammersSerializer


class LanguageView(viewsets.ModelViewSet):
    queryset = Languages.objects.all()
    serializer_class = LanguageSerializer


class ParadigmView(viewsets.ModelViewSet):
    queryset = Paradigm.objects.all()
    serializer_class = ParadigmSerializer


class ProgrammersView(viewsets.ModelViewSet):
    queryset = Programmers.objects.all()
    serializer_class = ProgrammersSerializer
