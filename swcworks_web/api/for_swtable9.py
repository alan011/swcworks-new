from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic         import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators      import method_decorator
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from datetime import datetime
import json, re

from swcworks_web.models import SWTable9
from swcworks_web import config
from .common_tools import get_user_group, json_load
from .fields_validate import vld_float

@login_required
def getAPIForSWTable9(request, *args, **kwargs):
    ret_data = {'data':[],'total':0}
    print("[%s] ==== Try to get data from `SWTable9`:\nuser: %s" % (timezone.now().strftime('%d/%b/%Y %H:%M:%S'), request.user.username))

    ### Get user's group and make queryset.
    user_group = get_user_group(request)
    if user_group == 'admin':
        queryset = SWTable9.objects.all()
    elif user_group is None:
        error_message = "ERROR: user forbidden."
        print(error_message)
        return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=403)
    else:
        queryset = SWTable9.objects.filter(province = user_group)

    ### make return data.
    ret_data['total'] = queryset.count()
    for obj in queryset.order_by('-id'):
        tmp_data = {'id'       : obj.id,
                    'province' : config.PROVINCE_DEFINE[obj.province],
                    'type'     : str(obj.t9_type),
                    'name'     : obj.name,
                    'description': obj.zyqkjs,
                    'areaUnit' : obj.kzddqhdwmc,
                    'num'      : str(obj.num),
                    'trzj'     : str(obj.trzj),
                    }
        ret_data['data'].append(tmp_data)

    print('SUCCESS: %d entries of data returned.' % ret_data['total'])
    return HttpResponse(json.dumps(ret_data), content_type='application/json')


@login_required
@csrf_exempt
def addAPIForSWTable9(request, *args, **kwargs):
    ret_data = {}
    print("[%s] ==== Try to add data to `SWTable9`:\nuser: %s" % (timezone.now().strftime('%d/%b/%Y %H:%M:%S'), request.user.username))

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
    if not post_data.get('type') or not re.search('^[0-9]+$',str(post_data['type'])):
        error_message = "ERROR: To add data failed. Field 'type' must be provided and should be a number."
        print(error_message)
        return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=400)
    else:
        attrs['t9_type'] = int(post_data['type'])

    if not post_data.get('name'):
        error_message = "ERROR: To add data failed. Field 'name' must be provided."
        print(error_message)
        return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=400)
    else:
        attrs['name'] = post_data['name']

    if not post_data.get('description'):
        error_message = "ERROR: To add data failed. Field 'description' must be provided."
        print(error_message)
        return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=400)
    else:
        attrs['zyqkjs'] = post_data['description']

    if not post_data.get('areaUnit'):
        error_message = "ERROR: To add data failed. Field 'areaUnit' must be provided."
        print(error_message)
        return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=400)
    else:
        attrs['kzddqhdwmc'] = post_data['areaUnit']

    if not post_data.get('num') or not re.search('^[0-9]+$', str(post_data.get('num'))):
        error_message = "ERROR: To add data failed. Field 'num' must be provided, and must be a Number."
        print(error_message)
        return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=400)
    else:
        attrs['num'] = int(post_data['num'])

    attrs['trzj'] = vld_float(post_data.get('trzj'))
    if attrs['trzj'] is None:
        error_message = "ERROR: To add data failed. Field 'trzj' must be provided, and must be a Number."
        print(error_message)
        return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=400)

    attrs['province'] = user_group
    attrs['reporter'] = request.user.username
    attrs['report_time'] = timezone.now()

    ### write data to db.
    obj = SWTable9(**attrs)
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
def deleteAPIForSWTable9(request, *args, **kwargs):
    print("[%s] ==== Try to delete data from `SWTable9`:\nuser: %s" % (timezone.now().strftime('%d/%b/%Y %H:%M:%S'), request.user.username))

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
    queryset = SWTable9.objects.filter(id=post_data['id'])
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

    print("SUCCESS: data with id=%s deleted from `SWTable9`." % post_data['id'])
    return HttpResponse(json.dumps({}), content_type='application/json')


@login_required
@csrf_exempt
def updateAPIForSWTable9(request, *args, **kwargs):
    print("[%s] ==== Try to update data in `SWTable9`:\nuser: %s" % (timezone.now().strftime('%d/%b/%Y %H:%M:%S'), request.user.username))

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
    queryset = SWTable9.objects.filter(id=post_data['id'])
    if queryset.exists():
        obj = queryset.get(id=post_data['id'])
    else:
        error_message = "ERROR: To update data failed, data with id=%s not exist." % post_data['id']
        print(error_message)
        return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=400)

    ### update obj.
    if post_data.get('type'):
        if re.search('^[0-9]+$',str(post_data['type'])):
            obj.t9_type = int(post_data['type'])
        else:
            error_message = "ERROR: 'type' field must be a number."
            print(error_message)
            return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=400)
    if post_data.get('num'):
        if re.search('^[0-9]+$',str(post_data['num'])):
            obj.num = int(post_data['num'])
        else:
            error_message = "ERROR: 'num' field must be a number."
            print(error_message)
            return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=400)
    if post_data.get('trzj') is not None:
        obj.trzj = vld_float(post_data['trzj'])
        if obj.trzj is None:
            error_message = "ERROR: 'trzj' field must be a number."
            print(error_message)
            return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=400)

    if post_data.get('name'):
        obj.name = post_data['name']
    if post_data.get('description'):
        obj.zyqkjs = post_data['description']
    if post_data.get('areaUnit'):
        obj.kzddqhdwmc = post_data['areaUnit']
    try:
        obj.save()
    except:
        error_message = "ERROR: To update data failed, DB error occured." % post_data['id']
        print(error_message)
        return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=400)

    print("SUCCESS: data with id=%s updated in `SWTable9`." % post_data['id'])
    return HttpResponse(json.dumps({}), content_type='application/json')
