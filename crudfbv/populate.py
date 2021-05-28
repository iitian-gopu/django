import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crudfbv.settings')

import django
django.setup()

from random import *
from testapp.models import *
from faker import Faker

faker = Faker()



def populate(N):
    for entry in range(N):                
        fake_no =randint(1001,9999)
        fake_sal = randint(10000,99999)
        fake_name = faker.name()
        fake_addr = faker.city()
        emp_record=Employee.objects.get_or_create(eno=fake_no,ename=fake_name,esal=fake_sal,eaddr=fake_addr)
populate(50)
