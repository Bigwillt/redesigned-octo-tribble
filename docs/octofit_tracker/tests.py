from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(email="test@example.com", name="Test User", age=25)
        self.assertEqual(user.email, "test@example.com")

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name="Team A", description="A test team")
        self.assertEqual(team.name, "Team A")

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        user = User.objects.create(email="test@example.com", name="Test User", age=25)
        activity = Activity.objects.create(user=user, description="Test Activity", timestamp="2025-04-08T12:00:00Z")
        self.assertEqual(activity.description, "Test Activity")

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        team = Team.objects.create(name="Team A", description="A test team")
        leaderboard = Leaderboard.objects.create(team=team, score=100)
        self.assertEqual(leaderboard.score, 100)

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        user = User.objects.create(email="test@example.com", name="Test User", age=25)
        workout = Workout.objects.create(user=user, type="Running", duration=30, calories_burned=300, timestamp="2025-04-08T12:00:00Z")
        self.assertEqual(workout.type, "Running")
