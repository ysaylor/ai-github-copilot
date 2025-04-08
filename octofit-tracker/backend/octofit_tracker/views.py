import os
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer
from .models import User, Team, Activity, Leaderboard, Workout
from django.conf import settings
from django.http import JsonResponse

@api_view(['GET'])
def api_root(request, format=None):
    base_url = settings.BASE_URL.rstrip('/')  # Ensure no trailing slash
    return JsonResponse({
        'users': f"{base_url}/api/users/?format=api",
        'teams': f"{base_url}/api/teams/?format=api",
        'activities': f"{base_url}/api/activities/?format=api",
        'leaderboard': f"{base_url}/api/leaderboard/?format=api",
        'workouts': f"{base_url}/api/workouts/?format=api"
    })

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class LeaderboardViewSet(viewsets.ModelViewSet):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer