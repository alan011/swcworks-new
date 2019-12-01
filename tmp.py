#!/usr/local/bin/python3

import os, sys, re, time, json, django, datetime
from collections import OrderedDict

sys.path.append('/var/django_projects/SWCWorks')
#os.environ['DJANGO_SETTING_MODULE']='geniusalt_project.settings'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SWCWorks.settings")
django.setup()


from swcworks_web.models import *

for field in SWTable1._meta.get_fields():
    print(field.name, field.verbose_name)
