# api/views.py
from rest_framework import viewsets, filters
from .models import *
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend # Importa DjangoFilterBackend

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter] # Usa DjangoFilterBackend
    ordering_fields = ['points']
    # filterset_fields = ['team_name'] # Esempio per filtrare i team per nome

class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    ordering_fields = ['points']
    filterset_fields = ['number', 'team__team_name', 'first_name', 'last_name', 'acronym'] # Esempio di filtri per i driver

class RaceViewSet(viewsets.ModelViewSet):
    queryset = Race.objects.all()
    serializer_class = RaceSerializer
    filter_backends = [DjangoFilterBackend] # Anche qui puoi aggiungere un filtro se vuoi
    filterset_fields = ['year', 'country_name', 'location', 'meeting_key'] # Filtra per anno, paese o meeting_key

class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['race__meeting_key', 'session_type', 'session_key'] # Filtra per meeting_key della gara, tipo di sessione o session_key

class ResultViewSet(viewsets.ModelViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['session__session_key', 'driver__number', 'position'] # Filtra per sessione o driver