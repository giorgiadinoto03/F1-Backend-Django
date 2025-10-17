from rest_framework import serializers
from .models import Team, Driver, Race, Session, Result
from django.conf import settings

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

class DriverSerializer(serializers.ModelSerializer):
    team_name = serializers.CharField(source='team.team_name', read_only=True)
    team_colo
    class Meta:
        model = Driver
        fields = '__all__'

class RaceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Race
        fields = '__all__'

class SessionSerializer(serializers.ModelSerializer):
    meeting_key = serializers.IntegerField(source='race.meeting_key', read_only=True)
    meeting_name = serializers.CharField(source='race.meeting_name', read_only=True)
    session_order_number = serializers.IntegerField(read_only=True) # Aggiunta per ordinare le sessioni in base ai parametri che vengono passati in views.

    class Meta:
        model = Session
        fields = ['session_key', 'session_name', 'session_type', 'date_start', 'meeting_key', 'meeting_name', 'session_order_number', 'circuit_short_name']

class ResultSerializer(serializers.ModelSerializer):
    driver_number = serializers.IntegerField(source='driver.number', read_only=True)
    name_acronym = serializers.CharField(source='driver.acronym', read_only=True)
    full_name = serializers.CharField(source='driver.full_name', read_only=True)
    team_name = serializers.CharField(source='driver.team.team_name', read_only=True)
    team_colour = serializers.CharField(source='driver.team.team_colour', read_only=True)
    headshot_url = serializers.CharField(source='driver.image_url', read_only=True)

    class Meta:
        model = Result
        fields = ['session', 'driver_number', 'name_acronym', 'full_name', 'team_name', 'team_colour', 'headshot_url', 'position', 'time', 'gap_to_leader', 'q1', 'q2', 'q3']

