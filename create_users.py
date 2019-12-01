#!/usr/local/python3

import os, sys, re, time, json, django

sys.path.append('/var/django_projects/SWCWorks')
#os.environ['DJANGO_SETTING_MODULE']='geniusalt_project.settings'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SWCWorks.settings")
django.setup()

from django.contrib.auth.models import Group, User
from swcworks_web.config import PROVINCE_DEFINE


if len(sys.argv) != 5:
    print("wrong usage.")
    sys.exit(1)

print("====> to add user: %s" % sys.argv[1])
user_name  = sys.argv[1]
real_name  = sys.argv[3]
group_name = sys.argv[4]
password   = sys.argv[2]

new_user = User.objects.create_user(username=user_name)

new_user.set_password(password)
new_user.first_name  = real_name


if group_name in PROVINCE_DEFINE:
    group_obj = Group.objects.get(name=group_name)
    new_user.groups.set([group_obj])
else:
    print("ERROR: group '%s' not exist. user: %s" % (group_name, user_name))

new_user.save()


