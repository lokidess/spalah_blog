from django.core.management.base import BaseCommand

from core.models import Post


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            '-n',
            '--numbers',
            dest='numbers',
            default=0
        )

    def handle(self, *args, **options):
        count = int(options['numbers'])
        for x in range(0, count):
            Post.objects.create(
                title=f'qwe{x}',
                body=f'qwe{x}',
                owner_id=1
            )
