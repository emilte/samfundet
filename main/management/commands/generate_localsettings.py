# imports
from django.core.management.base import BaseCommand
from django.utils import timezone
from django.core import management
from nbb.models import *
import json
from getpass import getpass
import random
import os

# End: imports -----------------------------------------------------------------

# Settings:
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def getDevSettings():
    s = "\n\n# Enable this to overwrite local_settings with dev_settings"
    s += "\nDEV_SETTINGS = False"
    s += "\n\ntry:"
    s += "\n\tif DEV_SETTINGS:"
    s += "\n\t\tfrom dev_settings import *"
    s += "\n\t\tprint('local_settings was overwritten by dev_settings')"
    s += "\nexcept:"
    s += "\n\t\tprint('')"
    return s

def getDatabase():
    choise = None
    options = {
        '1': 'django.db.backends.postgresql_psycopg2',
        '2': 'django.db.backends.sqlite3',
        '3': 'django.db.backends.postgresql',
    }

    print("\nChoose ENGINE:")
    for k, v in options.items():
        print('({}) {}'.format(k, v))

    while choise not in options.keys():
        choise = input(": ")

    ENGINE = options[choise]

    NAME = input("NAME: ")
    USER = input("USER: ")
    PASSWORD = getpass("PASSWORD: ")
    HOST = input("HOST: ")
    PORT = input("PORT: ")

    DATABASES = {
        'ENGINE': ENGINE,
        'NAME': NAME,
        'USER': USER,
        'PASSWORD': PASSWORD,
        'HOST': HOST,
        'PORT': PORT,
    }

    return "\n\nDATABASES = " + json.dumps(DATABASES, indent=4)






def getSecretKey():
    key = "".join( [random.choice("abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)") for i in range(50)] )
    return "\n\nSECRET_KEY = '{}'".format(key)


class Command(BaseCommand):

    def handle(self, *args, **options):
        filename = "generated_local_settings.py"
        path = os.path.join(BASE_DIR, "../" + filename)

        try:
            with open(path, mode="w+", encoding="UTF-8") as file:
                file.write(getSecretKey())
                file.write(getDatabase())
                file.write(getDevSettings())
                print("\nFile saved as '{}'".format(filename))
                print("== DONE ==")
        except:
            print("== ERROR ==")
