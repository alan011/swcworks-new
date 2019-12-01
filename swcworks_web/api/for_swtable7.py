from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic         import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators      import method_decorator
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from datetime import datetime
import json, re

from swcworks_web.models import SWTable7
from swcworks_web import config
from .common_tools import get_user_group, json_load

@login_required
def getAPIForSWTable7(request, *args, **kwargs):
    ret_data = {'data':[],'total':0}
    print("[%s] ==== Try to get data from `SWTable7`:\nuser: %s" % (timezone.now().strftime('%d/%b/%Y %H:%M:%S'), request.user.username))

    ### Get user's group and make queryset.
    user_group = get_user_group(request)
    if user_group == 'admin':
        queryset = SWTable7.objects.all()
    elif user_group is None:
        error_message = "ERROR: user forbidden."
        print(error_message)
        return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=403)
    else:
        queryset = SWTable7.objects.filter(province = user_group)

    ### make return data.
    ret_data['total'] = queryset.count()
    for obj in queryset.order_by('-id'):
        tmp_data = {'id'         : obj.id,
                    'province'   : config.PROVINCE_DEFINE[obj.province],
                    'level'      : str(obj.level),
                    'jigouNum'   : str(obj.jgsl),
                    'zhuanzhiNum': str(obj.zzgzrysl),
                    'jicengNum'  : str(obj.jcdzzsl),
                    'dangyuanNum': str(obj.dysl),
                    }
        ret_data['data'].append(tmp_data)

    print('SUCCESS: %d entries of data returned.' % ret_data['total'])
    return HttpResponse(json.dumps(ret_data), content_type='application/json')


@login_required
@csrf_exempt
def addAPIForSWTable7(request, *args, **kwargs):
    ret_data = {}
    print("[%s] ==== Try to add data to `SWTable7`:\nuser: %s" % (timezone.now().strftime('%d/%b/%Y %H:%M:%S'), request.user.username))

    ### Check user group.
    user_group = get_user_group(request)
    if user_group is None or user_group == 'admin':
        error_message = 'ERROR: user forbidden.'
        print(error_message)
        return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=403)

    ### Load json data.
    # post_data = json_load(request)
    # if isinstance(post_data, str):
    #     return HttpResponse(json.dumps({'message':post_data}), content_type='application/json', status=400)
    post_data = {key:request.POST.get(key) for key in request.POST.keys()}
    print(post_data)

    ### make obj attrs.
    attrs = {}
    if not post_data.get('level') or not re.search('^[0-9]+$',str(post_data['level'])):
        error_message = "ERROR: To add data failed. Field 'level' must be provided and should be a number."
        print(error_message)
        return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=400)
    else:
        attrs['level'] = int(post_data['level'])

    if not post_data.get('jigouNum') or not re.search('^[0-9]+$',str(post_data['jigouNum'])):
        error_message = "ERROR: To add data failed. Field 'jigouNum' must be provided and should be a number."
        print(error_message)
        return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=400)
    else:
        attrs['jgsl'] = int(post_data['jigouNum'])

    if not post_data.get('zhuanzhiNum') or not re.search('^[0-9]+$',str(post_data['zhuanzhiNum'])):
        error_message = "ERROR: To add data failed. Field 'zhuanzhiNum' must be provided and should be a number."
        print(error_message)
        return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=400)
    else:
        attrs['zzgzrysl'] = int(post_data['zhuanzhiNum'])

    if not post_data.get('jicengNum') or not re.search('^[0-9]+$',str(post_data['jicengNum'])):
        error_message = "ERROR: To add data failed. Field 'jicengNum' must be provided and should be a number."
        print(error_message)
        return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=400)
    else:
        attrs['jcdzzsl'] = int(post_data['jicengNum'])

    if not post_data.get('dangyuanNum') or not re.search('^[0-9]+$',str(post_data['dangyuanNum'])):
        error_message = "ERROR: To add data failed. Field 'dangyuanNum' must be provided and should be a number."
        print(error_message)
        return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=400)
    else:
        attrs['dysl'] = int(post_data['dangyuanNum'])

    attrs['province'] = user_group
    attrs['reporter'] = request.user.username
    attrs['report_time'] = timezone.now()

    ### write data to db.
    obj = SWTable7(**attrs)
    try:
        obj.save()
    except:
        error_message = "ERROR: To write data to db failed."
        print(error_message)
        return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=500)

    ### make return data.
    ret_data['id'] = obj.id
    ret_data['province'] = config.PROVINCE_DEFINE[user_group]

    return HttpResponse(json.dumps(ret_data), content_type='application/json')


@login_required
@csrf_exempt
def deleteAPIForSWTable7(request, *args, **kwargs):
    print("[%s] ==== Try to delete data from `SWTable7`:\nuser: %s" % (timezone.now().strftime('%d/%b/%Y %H:%M:%S'), request.user.username))

    ### Get user's group and make queryset.
    user_group = get_user_group(request)
    if user_group is None:
        error_message = "ERROR: user forbidden."
        print(error_message)
        return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=403)

    ### Load json data.
    # post_data = json_load(request)
    # if isinstance(post_data, str):
    #     return HttpResponse(json.dumps({'message':post_data}), content_type='application/json', status=400)
    post_data = {key:request.POST.get(key) for key in request.POST.keys()}
    print(post_data)

    ### make data query.
    if 'id' not in post_data or not re.search('^[0-9]+$', str(post_data['id'])):
        post_data['id'] = int(post_data['id'])
        error_message = "ERROR: To delete data failed. Illegal data id."
        print(error_message)
        return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=400)
    queryset = SWTable7.objects.filter(id=post_data['id'])
    if queryset.exists():
        obj = queryset.get(id=post_data['id'])
        if user_group != 'admin' and obj.province != user_group:
            error_message = "ERROR: user forbidden, province not match."
            print(error_message)
            return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=403)

        try:
            obj.delete()
        except:
            error_message = "ERROR: To delete data failed, DB error ocurred."
            print(error_message)
            return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=500)

    print("SUCCESS: data with id=%s deleted from `SWTable7`." % post_data['id'])
    return HttpResponse(json.dumps({}), content_type='application/json')


@login_required
@csrf_exempt
def updateAPIForSWTable7(request, *args, **kwargs):
    print("[%s] ==== Try to update data in `SWTable7`:\nuser: %s" % (timezone.now().strftime('%d/%b/%Y %H:%M:%S'), request.user.username))

    ### Get user's group and make queryset.
    user_group = get_user_group(request)
    if user_group is None:
        error_message = "ERROR: user forbidden."
        print(error_message)
        return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=403)

    ### Load json data.
    # post_data = json_load(request)
    # if isinstance(post_data, str):
    #     return HttpResponse(json.dumps({'message':post_data}), content_type='application/json', status=400)
    post_data = {key:request.POST.get(key) for key in request.POST.keys()}
    print(post_data)

    ### make data query.
    if not post_data.get('id') or not re.search('^[0-9]+$', str(post_data['id'])):
        post_data['id'] = int(post_data['id'])
        error_message = "ERROR: To update data failed. Illegal data id."
        print(error_message)
        return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=400)
    queryset = SWTable7.objects.filter(id=post_data['id'])
    if queryset.exists():
        obj = queryset.get(id=post_data['id'])
    else:
        error_message = "ERROR: To update data failed, data with id=%s not exist." % post_data['id']
        print(error_message)
        return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=400)

    ### update obj.
    if post_data.get('level'):
        if re.search('^[0-9]+$',str(post_data['level'])):
            obj.level = int(post_data['level'])
        else:
            error_message = "ERROR: 'level' field must be a number."
            print(error_message)
            return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=400)

    if post_data.get('jigouNum'):
        if re.search('^[0-9]+$',str(post_data['jigouNum'])):
            obj.jgsl = int(post_data['jigouNum'])
        else:
            error_message = "ERROR: 'jigouNum' field must be a number."
            print(error_message)
            return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=400)

    if post_data.get('zhuanzhiNum'):
        if re.search('^[0-9]+$',str(post_data['zhuanzhiNum'])):
            obj.zzgzrysl = int(post_data['zhuanzhiNum'])
        else:
            error_message = "ERROR: 'zhuanzhiNum' field must be a number."
            print(error_message)
            return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=400)

    if post_data.get('jicengNum'):
        if re.search('^[0-9]+$',str(post_data['jicengNum'])):
            obj.jcdzzsl = int(post_data['jicengNum'])
        else:
            error_message = "ERROR: 'jicengNum' field must be a number."
            print(error_message)
            return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=400)

    if post_data.get('dangyuanNum'):
        if re.search('^[0-9]+$',str(post_data['dangyuanNum'])):
            obj.dysl = int(post_data['dangyuanNum'])
        else:
            error_message = "ERROR: 'dangyuanNum' field must be a number."
            print(error_message)
            return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=400)

    try:
        obj.save()
    except:
        error_message = "ERROR: To update data failed, DB error occured." % post_data['id']
        print(error_message)
        return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=400)

    print("SUCCESS: data with id=%s updated in `SWTable7`." % post_data['id'])
    return HttpResponse(json.dumps({}), content_type='application/json')
