from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel', description='Marvel Team')
        dc = Team.objects.create(name='DC', description='DC Team')

        # Create users
        ironman = User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel)
        spiderman = User.objects.create(name='Spider Man', email='spiderman@marvel.com', team=marvel)
        batman = User.objects.create(name='Batman', email='batman@dc.com', team=dc)
        superman = User.objects.create(name='Superman', email='superman@dc.com', team=dc)

        # Create activities
        Activity.objects.create(user=ironman, type='Running', duration=30, calories=300, date=timezone.now().date())
        Activity.objects.create(user=spiderman, type='Cycling', duration=45, calories=400, date=timezone.now().date())
        Activity.objects.create(user=batman, type='Swimming', duration=60, calories=500, date=timezone.now().date())
        Activity.objects.create(user=superman, type='Yoga', duration=20, calories=100, date=timezone.now().date())

        # Create workouts
        pushups = Workout.objects.create(name='Push Ups', description='Upper body workout')
        yoga = Workout.objects.create(name='Yoga Routine', description='Flexibility workout')
        pushups.suggested_for.add(ironman, batman)
        yoga.suggested_for.add(spiderman, superman)

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, points=700)
        Leaderboard.objects.create(team=dc, points=600)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully!'))
