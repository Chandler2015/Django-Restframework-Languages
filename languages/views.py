from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Languages, Paradigm, Programmers
from .serializers import LanguageSerializer, ParadigmSerializer, ProgrammersSerializer


class LanguageView(viewsets.ModelViewSet):
    queryset = Languages.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class ParadigmView(viewsets.ModelViewSet):
    queryset = Paradigm.objects.all()
    serializer_class = ParadigmSerializer


class ProgrammersView(viewsets.ModelViewSet):
    queryset = Programmers.objects.all()
    serializer_class = ProgrammersSerializer
