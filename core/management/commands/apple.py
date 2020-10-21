from os import system
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    '''
        This is just for test!!!!
    '''
    help = 'Apple!'

    def add_arguments(self, parser):
        parser.add_argument('fruit', type=str)

    def handle(self, *args, **options):
        system(f'python manage.py startapp { options["fruit"] }')
