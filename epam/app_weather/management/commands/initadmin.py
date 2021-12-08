from django.contrib.auth.models import User
from django.core.management import BaseCommand

from epam.settings import env


class Command(BaseCommand):

    def handle(self, *args, **options):
        if not User.objects.count():
            admin = User.objects.create_superuser(username=env('ADMIN'), password=env('PASSWORD'),
                                                  email='admin@admin.ru')
            admin.is_active = True
            admin.is_admin = True
            admin.save()
