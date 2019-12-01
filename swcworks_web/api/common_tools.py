from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic         import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators      import method_decorator
from django.utils import timezone
import json, os

def get_user_group(request):
    # user_group = 'Beijing'
    user_group_queryset = request.user.groups.all()
    user_groups = []
    for obj in user_group_queryset:
        user_groups.append(obj.name)

    print('group: %s' % str(user_groups))
    if len(user_groups) == 1:
        return user_groups[0]
    else:
        if len(user_groups) != 0:
            print("Warning: user '%s' belongs to more than one groups, this will treat user as no permission user." % request.user.username)
        return None

def json_load(request, decode_type='utf-8'):
    try:
        post_data   = json.loads(request.body.decode(decode_type))
    except:
        return "ERROR: To load json data failed."

    print(post_data)
    if isinstance(post_data, dict):
        return post_data
    else:
        return "ERROR: Post data illegal."

def get_file_list(file_path):
    file_list = []
    if os.path.isdir(file_path):
        for file_name in os.listdir(file_path):
            file_list.append(file_name)
    return file_list
