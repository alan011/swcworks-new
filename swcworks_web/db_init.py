from django.contrib.auth.models import Group
from .config import PROVINCE_DEFINE

def groups_init():
    group_names = list(PROVINCE_DEFINE.keys())
    group_names.append('admin')
    for group_name in group_names:
        if not Group.objects.filter(name=group_name).exists():
            group_obj = Group(name=group_name)
            group_obj.save()
            print("NOTE: groups_init(): %s added to db successfully." % group_name)
