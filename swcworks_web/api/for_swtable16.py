from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic         import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators      import method_decorator
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from datetime import datetime
import json, re, os

from swcworks_web.models import SWTable16
from swcworks_web import config
from .common_tools import get_user_group, json_load, get_file_list
from .fields_validate import vld_float


@login_required
def getAPIForSWTable16(request, *args, **kwargs):
    ret_data = {'data':[],'total':0}
    print("[%s] ==== Try to get data from `SWTable16`:\nuser: %s" % (timezone.now().strftime('%d/%b/%Y %H:%M:%S'), request.user.username))

    ### Get user's group and make queryset.
    user_group = get_user_group(request)
    if user_group == 'admin':
        queryset = SWTable16.objects.all()
    elif user_group is None:
        error_message = "ERROR: user forbidden."
        print(error_message)
        return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=403)
    else:
        queryset = SWTable16.objects.filter(province = user_group)

    ### make return data.
    ret_data['total'] = queryset.count()
    for obj in queryset.order_by('-id'):
        tmp_data = {'id'         : obj.id,
                    'province'   : config.PROVINCE_DEFINE[obj.province],
                    'measure'    : obj.zyzccs,
                    'czzj'       : str(obj.czzjtr),
                    'fcj'        : str(obj.fcjtr),
                    }
        ret_data['data'].append(tmp_data)

    user_storage = os.path.join(config.FILE_STORAGE_ROOT, user_group, request.user.username, 'table16')
    ret_data['fileList'] = get_file_list(user_storage)
    print('SUCCESS: %d entries of data returned.' % ret_data['total'])
    return HttpResponse(json.dumps(ret_data), content_type='application/json')


@login_required
@csrf_exempt
def addAPIForSWTable16(request, *args, **kwargs):
    ret_data = {}
    print("[%s] ==== Try to add data to `SWTable16`:\nuser: %s" % (timezone.now().strftime('%d/%b/%Y %H:%M:%S'), request.user.username))

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
    if not post_data.get('measure'):
        error_message = "ERROR: To add data failed. Field 'measure' must be provided."
        print(error_message)
        return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=400)
    else:
        attrs['zyzccs'] = post_data['measure']

    attrs['czzjtr'] = vld_float(post_data['czzj'])
    if attrs['czzjtr'] is None:
        error_message = "ERROR: To add data failed. Field 'czzj' must be provided and should be a number."
        print(error_message)
        return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=400)

    attrs['fcjtr'] = vld_float(post_data['fcj'])
    if attrs['fcjtr'] is None:
        error_message = "ERROR: To add data failed. Field 'fcj' must be provided and should be a number."
        print(error_message)
        return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=400)

    attrs['province'] = user_group
    attrs['reporter'] = request.user.username
    attrs['report_time'] = timezone.now()

    ### write data to db.
    obj = SWTable16(**attrs)
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
def deleteAPIForSWTable16(request, *args, **kwargs):
    print("[%s] ==== Try to delete data from `SWTable16`:\nuser: %s" % (timezone.now().strftime('%d/%b/%Y %H:%M:%S'), request.user.username))

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
    queryset = SWTable16.objects.filter(id=post_data['id'])
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

    print("SUCCESS: data with id=%s deleted from `SWTable16`." % post_data['id'])
    return HttpResponse(json.dumps({}), content_type='application/json')


@login_required
@csrf_exempt
def updateAPIForSWTable16(request, *args, **kwargs):
    print("[%s] ==== Try to update data in `SWTable16`:\nuser: %s" % (timezone.now().strftime('%d/%b/%Y %H:%M:%S'), request.user.username))

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
    queryset = SWTable16.objects.filter(id=post_data['id'])
    if queryset.exists():
        obj = queryset.get(id=post_data['id'])
    else:
        error_message = "ERROR: To update data failed, data with id=%s not exist." % post_data['id']
        print(error_message)
        return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=400)

    ### update obj.
    if post_data.get('czzj') is not None:
        obj.czzjtr = vld_float(post_data['czzj'])
        if obj.czzjtr is None:
            error_message = "ERROR: 'czzj' field must be a number."
            print(error_message)
            return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=400)
    if post_data.get('fcj') is not None:
        obj.fcjtr = vld_float(post_data['fcj'])
        if obj.fcjtr is None:
            error_message = "ERROR: 'fcj' field must be a number."
            print(error_message)
            return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=400)

    if post_data.get('measure') is not None:
        obj.zyzccs = post_data['measure']

    try:
        obj.save()
    except:
        error_message = "ERROR: To update data failed, DB error occured." % post_data['id']
        print(error_message)
        return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=400)

    print("SUCCESS: data with id=%s updated in `SWTable16`." % post_data['id'])
    return HttpResponse(json.dumps({}), content_type='application/json')
