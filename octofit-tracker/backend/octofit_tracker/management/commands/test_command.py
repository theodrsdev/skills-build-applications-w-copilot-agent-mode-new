from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Test command to verify BaseCommand import'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('BaseCommand import is working correctly.'))
