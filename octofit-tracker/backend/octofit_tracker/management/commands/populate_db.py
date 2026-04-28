from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

from octofit_tracker import models as octo_models

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Usuń istniejące dane
        User.objects.all().delete()
        octo_models.Team.objects.all().delete()
        octo_models.Activity.objects.all().delete()
        octo_models.Leaderboard.objects.all().delete()
        octo_models.Workout.objects.all().delete()

        # Tworzenie drużyn
        marvel = octo_models.Team.objects.create(name='Marvel')
        dc = octo_models.Team.objects.create(name='DC')

        # Tworzenie użytkowników
        ironman = User.objects.create_user(username='ironman', email='ironman@marvel.com', password='test', team=marvel)
        captain = User.objects.create_user(username='captain', email='captain@marvel.com', password='test', team=marvel)
        batman = User.objects.create_user(username='batman', email='batman@dc.com', password='test', team=dc)
        superman = User.objects.create_user(username='superman', email='superman@dc.com', password='test', team=dc)

        # Tworzenie aktywności
        octo_models.Activity.objects.create(user=ironman, type='run', duration=30)
        octo_models.Activity.objects.create(user=batman, type='cycle', duration=45)

        # Tworzenie leaderboard
        octo_models.Leaderboard.objects.create(user=ironman, points=100)
        octo_models.Leaderboard.objects.create(user=batman, points=120)

        # Tworzenie workoutów
        octo_models.Workout.objects.create(name='Pushups', description='Do 20 pushups')
        octo_models.Workout.objects.create(name='Situps', description='Do 30 situps')

        self.stdout.write(self.style.SUCCESS('Baza octofit_db została wypełniona przykładowymi danymi.'))
