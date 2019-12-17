from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic         import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators      import method_decorator
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from datetime import datetime
import json, re, os

from swcworks_web.models import SWTable14
from swcworks_web import config
from .common_tools import get_user_group, json_load, get_file_list

@login_required
def getAPIForSWTable14(request, *args, **kwargs):
    ret_data = {'data':[],'total':0}
    print("[%s] ==== Try to get data from `SWTable14`:\nuser: %s" % (timezone.now().strftime('%d/%b/%Y %H:%M:%S'), request.user.username))

    ### Get user's group and make queryset.
    user_group = get_user_group(request)
    if user_group == 'admin':
        queryset = SWTable14.objects.all()
    elif user_group is None:
        error_message = "ERROR: user forbidden."
        print(error_message)
        return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=403)
    else:
        queryset = SWTable14.objects.filter(province = user_group)

    ### make return data.
    ret_data['total'] = queryset.count()
    for obj in queryset.order_by('-id'):
        tmp_data = {'id'         : obj.id,
                    'province'   : config.PROVINCE_DEFINE[obj.province],
                    'areaName'   : obj.area_name,
                    'num1'       : str(obj.xsl),
                    'num2'       : str(obj.jsl),
                    'num3'       : str(obj.sqsl),
                    'num4'       : str(obj.dwsl),
                    }
        ret_data['data'].append(tmp_data)

    user_storage = os.path.join(config.FILE_STORAGE_ROOT, user_group, request.user.username, 'table15')
    ret_data['fileList'] = get_file_list(user_storage)
    print('SUCCESS: %d entries of data returned.' % ret_data['total'])
    return HttpResponse(json.dumps(ret_data), content_type='application/json')


@login_required
@csrf_exempt
def addAPIForSWTable14(request, *args, **kwargs):
    ret_data = {}
    print("[%s] ==== Try to add data to `SWTable14`:\nuser: %s" % (timezone.now().strftime('%d/%b/%Y %H:%M:%S'), request.user.username))

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
    if not post_data.get('areaName'):
        error_message = "ERROR: To add data failed. Field 'areaName' must be provided."
        print(error_message)
        return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=400)
    else:
        attrs['area_name'] = post_data['areaName']

    if not post_data.get('num1') or not re.search('^[0-9]+$',str(post_data['num1'])):
        error_message = "ERROR: To add data failed. Field 'num1' must be provided and should be a number."
        print(error_message)
        return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=400)
    else:
        attrs['xsl'] = int(post_data['num1'])

    if not post_data.get('num2') or not re.search('^[0-9]+$',str(post_data['num2'])):
        error_message = "ERROR: To add data failed. Field 'num2' must be provided and should be a number."
        print(error_message)
        return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=400)
    else:
        attrs['jsl'] = int(post_data['num2'])

    if not post_data.get('num3') or not re.search('^[0-9]+$',str(post_data['num3'])):
        error_message = "ERROR: To add data failed. Field 'num3' must be provided and should be a number."
        print(error_message)
        return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=400)
    else:
        attrs['sqsl'] = int(post_data['num3'])

    if not post_data.get('num4') or not re.search('^[0-9]+$',str(post_data['num4'])):
        error_message = "ERROR: To add data failed. Field 'num4' must be provided and should be a number."
        print(error_message)
        return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=400)
    else:
        attrs['dwsl'] = int(post_data['num4'])

    attrs['province'] = user_group
    attrs['reporter'] = request.user.username
    attrs['report_time'] = timezone.now()

    ### write data to db.
    obj = SWTable14(**attrs)
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
def deleteAPIForSWTable14(request, *args, **kwargs):
    print("[%s] ==== Try to delete data from `SWTable14`:\nuser: %s" % (timezone.now().strftime('%d/%b/%Y %H:%M:%S'), request.user.username))

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
    queryset = SWTable14.objects.filter(id=post_data['id'])
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

    print("SUCCESS: data with id=%s deleted from `SWTable14`." % post_data['id'])
    return HttpResponse(json.dumps({}), content_type='application/json')


@login_required
@csrf_exempt
def updateAPIForSWTable14(request, *args, **kwargs):
    print("[%s] ==== Try to update data in `SWTable14`:\nuser: %s" % (timezone.now().strftime('%d/%b/%Y %H:%M:%S'), request.user.username))

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
    queryset = SWTable14.objects.filter(id=post_data['id'])
    if queryset.exists():
        obj = queryset.get(id=post_data['id'])
    else:
        error_message = "ERROR: To update data failed, data with id=%s not exist." % post_data['id']
        print(error_message)
        return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=400)

    ### update obj.
    if post_data.get('areaName'):
        obj.area_name = post_data['areaName']

    if post_data.get('num1'):
        if re.search('^[0-9]+$',str(post_data['num1'])):
            obj.xsl = int(post_data['num1'])
        else:
            error_message = "ERROR: 'num1' field must be a number."
            print(error_message)
            return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=400)
    if post_data.get('num2'):
        if re.search('^[0-9]+$',str(post_data['num2'])):
            obj.jsl = int(post_data['num2'])
        else:
            error_message = "ERROR: 'num2' field must be a number."
            print(error_message)
            return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=400)
    if post_data.get('num3'):
        if re.search('^[0-9]+$',str(post_data['num3'])):
            obj.sqsl = int(post_data['num3'])
        else:
            error_message = "ERROR: 'num3' field must be a number."
            print(error_message)
            return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=400)
    if post_data.get('num4'):
        if re.search('^[0-9]+$',str(post_data['num4'])):
            obj.dwsl = int(post_data['num4'])
        else:
            error_message = "ERROR: 'num4' field must be a number."
            print(error_message)
            return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=400)

    try:
        obj.save()
    except:
        error_message = "ERROR: To update data failed, DB error occured." % post_data['id']
        print(error_message)
        return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=400)

    print("SUCCESS: data with id=%s updated in `SWTable14`." % post_data['id'])
    return HttpResponse(json.dumps({}), content_type='application/json')
