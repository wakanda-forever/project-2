import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
import django
django.setup()

import random
from myapp.models import User
from faker import Faker

fk = Faker()

def fake_pop(N=5):

    for _ in range (N):
        first = fk.first_name()
        last = fk.last_name()
        mail = fk.email()

        user = User.objects.create(first_name=first, last_name=last, email=mail)

if __name__ == '__main__':
    print("Populating")
    fake_pop(10)
    print("Complete")
