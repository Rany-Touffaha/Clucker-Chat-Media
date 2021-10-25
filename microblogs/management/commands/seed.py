from django.core.management.base import BaseCommand, CommandError
from faker import Faker
from microblogs.models import User


class Command(BaseCommand):
    def __init__(self):
        super().__init__()
        self.faker = Faker('en_GB')

    def handle(self, *args, **options):
        for i in range(1, 100):
            try:
                fakeUser = User.objects.create_user(username='@' + self.faker.user_name(),
                                                    password=self.faker.password(), first_name=self.faker.first_name(),
                                                    last_name=self.faker.last_name(), email=self.faker.email(), bio=self.faker.text())
                if fakeUser.full_clean():
                    fakeUser.save()
            except User.DoesNotExist:
                raise CommandError('Could not add user')


