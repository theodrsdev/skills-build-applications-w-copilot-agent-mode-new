from django.core.management.base import BaseCommand
from bson import ObjectId
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import timedelta

class Command(BaseCommand):
    help = 'Fully restore populate_db functionality'

    def handle(self, *args, **kwargs):
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        user1 = User.objects.create(_id=ObjectId(), username='testuser1', email='testuser1@example.com', password='password1')
        user2 = User.objects.create(_id=ObjectId(), username='testuser2', email='testuser2@example.com', password='password2')

        team = Team.objects.create(_id=ObjectId(), name='Test Team')
        team.members.add(user1, user2)

        activities = [
            Activity(_id=ObjectId(), user=user1, activity_type='Cycling', duration=timedelta(hours=1)),
            Activity(_id=ObjectId(), user=user2, activity_type='Running', duration=timedelta(hours=1, minutes=30)),
        ]
        Activity.objects.bulk_create(activities)

        leaderboard_entries = [
            Leaderboard(_id=ObjectId(), user=user1, score=100),
            Leaderboard(_id=ObjectId(), user=user2, score=90),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        workouts = [
            Workout(_id=ObjectId(), name='Cycling Training', description='Training for a road cycling event'),
            Workout(_id=ObjectId(), name='Running Training', description='Training for a marathon'),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Database populated with full test data.'))
