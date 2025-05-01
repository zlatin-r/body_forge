from django.core.management import call_command
from django.core.management.base import BaseCommand




class Command(BaseCommand):
    def handle(self, *args, **options):
        call_command("makemigrations")
        call_command("migrate")
        call_command("runserver")
