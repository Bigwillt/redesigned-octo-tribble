from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Define API root and include routes for users, teams, activity, leaderboard, and workouts
router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
]
