from django.contrib import admin
from .models import User, Team, Activity, Leaderboard, Workout

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("email", "name", "age", "created_at")

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "created_at")

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ("activity_id", "user", "description", "timestamp")

@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
    list_display = ("leaderboard_id", "team", "score", "updated_at")

@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ("workout_id", "user", "type", "duration", "calories_burned", "timestamp")
