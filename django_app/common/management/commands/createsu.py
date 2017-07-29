from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

from mysite.settings import config

UserModel = get_user_model()


class Command(BaseCommand):
    def handle(self, *args, **options):
        username = config['django']['defaultSuperuser']['username']
        password = config['django']['defaultSuperuser']['password']
        email = config['django']['defaultSuperuser']['email']
        if not UserModel.objects.filter(username=username).exists():
            UserModel.objects.create_superuser(
                username=username,
                password=password,
                email=email
            )
        else:
            print('default superuser exist')
