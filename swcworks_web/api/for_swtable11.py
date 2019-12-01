from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic         import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators      import method_decorator
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from datetime import datetime
import json, re, os

from swcworks_web.models import SWTable11
from swcworks_web import config
from .common_tools import get_user_group, json_load, get_file_list

@login_required
def getAPIForSWTable11(request, *args, **kwargs):
    ret_data = {'data':[],'total':0}
    print("[%s] ==== Try to get data from `SWTable11`:\nuser: %s" % (timezone.now().strftime('%d/%b/%Y %H:%M:%S'), request.user.username))

    ### Get user's group and make queryset.
    user_group = get_user_group(request)
    if user_group == 'admin':
        queryset = SWTable11.objects.all()
    elif user_group is None:
        error_message = "ERROR: user forbidden."
        print(error_message)
        return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=403)
    else:
        queryset = SWTable11.objects.filter(province = user_group)

    ### make return data.
    ret_data['total'] = queryset.count()
    for obj in queryset.order_by('-id'):
        tmp_data = {'id'         : obj.id,
                    'province'   : config.PROVINCE_DEFINE[obj.province],
                    'level'      : str(obj.level),
                    'areaName'   : obj.area_name,
                    'shtt'       : str(obj.shtt),
                    'shfwjg'     : str(obj.shfwjg),
                    'jjh'        : str(obj.jjh),
                    'innerOrgNum': str(obj.zyfwzzs),
                    'sqTotalNum' : str(obj.sqtotalnum),
                    'totalNum' : str(obj.totalnum),
                    }
        ret_data['data'].append(tmp_data)

    user_storage = os.path.join(config.FILE_STORAGE_ROOT, user_group, request.user.username, 'table11')
    ret_data['fileList'] = get_file_list(user_storage)
    print('SUCCESS: %d entries of data returned.' % ret_data['total'])
    return HttpResponse(json.dumps(ret_data), content_type='application/json')


@login_required
@csrf_exempt
def addAPIForSWTable11(request, *args, **kwargs):
    ret_data = {}
    print("[%s] ==== Try to add data to `SWTable11`:\nuser: %s" % (timezone.now().strftime('%d/%b/%Y %H:%M:%S'), request.user.username))

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

    if post_data.get('areaName'):
        attrs['area_name'] = post_data['areaName']

    if not post_data.get('shtt') or not re.search('^[0-9]+$',str(post_data['shtt'])):
        error_message = "ERROR: To add data failed. Field 'shtt' must be provided and should be a number."
        print(error_message)
        return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=400)
    else:
        attrs['shtt'] = int(post_data['shtt'])

    if not post_data.get('shfwjg') or not re.search('^[0-9]+$',str(post_data['shfwjg'])):
        error_message = "ERROR: To add data failed. Field 'shfwjg' must be provided and should be a number."
        print(error_message)
        return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=400)
    else:
        attrs['shfwjg'] = int(post_data['shfwjg'])

    if not post_data.get('jjh') or not re.search('^[0-9]+$',str(post_data['jjh'])):
        error_message = "ERROR: To add data failed. Field 'jjh' must be provided and should be a number."
        print(error_message)
        return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=400)
    else:
        attrs['jjh'] = int(post_data['jjh'])

    if not post_data.get('innerOrgNum') or not re.search('^[0-9]+$',str(post_data['innerOrgNum'])):
        error_message = "ERROR: To add data failed. Field 'innerOrgNum' must be provided and should be a number."
        print(error_message)
        return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=400)
    else:
        attrs['zyfwzzs'] = int(post_data['innerOrgNum'])

    if post_data.get('sqTotalNum'):
        if not re.search('^[0-9]+$',str(post_data['sqTotalNum'])):
            error_message = "ERROR: To add data failed. Field 'sqTotalNum' must be a number."
            print(error_message)
            return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=400)
        else:
            attrs['sqtotalnum'] = int(post_data['sqTotalNum'])

    if post_data.get('totalNum'):
        if not re.search('^[0-9]+$',str(post_data['totalNum'])):
            error_message = "ERROR: To add data failed. Field 'totalNum' must be a number."
            print(error_message)
            return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=400)
        else:
            attrs['totalnum'] = int(post_data['totalNum'])

    attrs['province'] = user_group
    attrs['reporter'] = request.user.username
    attrs['report_time'] = timezone.now()

    ### write data to db.
    obj = SWTable11(**attrs)
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
def deleteAPIForSWTable11(request, *args, **kwargs):
    print("[%s] ==== Try to delete data from `SWTable11`:\nuser: %s" % (timezone.now().strftime('%d/%b/%Y %H:%M:%S'), request.user.username))

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
    queryset = SWTable11.objects.filter(id=post_data['id'])
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

    print("SUCCESS: data with id=%s deleted from `SWTable11`." % post_data['id'])
    return HttpResponse(json.dumps({}), content_type='application/json')


@login_required
@csrf_exempt
def updateAPIForSWTable11(request, *args, **kwargs):
    print("[%s] ==== Try to update data in `SWTable11`:\nuser: %s" % (timezone.now().strftime('%d/%b/%Y %H:%M:%S'), request.user.username))

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
    queryset = SWTable11.objects.filter(id=post_data['id'])
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

    if post_data.get('areaName'):
        obj.area_name = post_data['areaName']

    if post_data.get('shtt'):
        if re.search('^[0-9]+$',str(post_data['shtt'])):
            obj.shtt = int(post_data['shtt'])
        else:
            error_message = "ERROR: 'shtt' field must be a number."
            print(error_message)
            return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=400)

    if post_data.get('shfwjg'):
        if re.search('^[0-9]+$',str(post_data['shfwjg'])):
            obj.shfwjg = int(post_data['shfwjg'])
        else:
            error_message = "ERROR: 'shfwjg' field must be a number."
            print(error_message)
            return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=400)
    if post_data.get('jjh'):
        if re.search('^[0-9]+$',str(post_data['jjh'])):
            obj.jjh = int(post_data['jjh'])
        else:
            error_message = "ERROR: 'jjh' field must be a number."
            print(error_message)
            return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=400)
    if post_data.get('innerOrgNum'):
        if re.search('^[0-9]+$',str(post_data['innerOrgNum'])):
            obj.zyfwzzs = int(post_data['innerOrgNum'])
        else:
            error_message = "ERROR: 'innerOrgNum' field must be a number."
            print(error_message)
            return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=400)

    if post_data.get('sqTotalNum'):
        if not re.search('^[0-9]+$',str(post_data['sqTotalNum'])):
            error_message = "ERROR: To modify data failed. Field 'sqTotalNum' must be a number."
            print(error_message)
            return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=400)
        else:
            obj.sqtotalnum = int(post_data['sqTotalNum'])
    if post_data.get('totalNum'):
        if not re.search('^[0-9]+$',str(post_data['totalNum'])):
            error_message = "ERROR: To modify data failed. Field 'totalNum' must be a number."
            print(error_message)
            return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=400)
        else:
            obj.totalnum = int(post_data['totalNum'])


    try:
        obj.save()
    except:
        error_message = "ERROR: To update data failed, DB error occured." % post_data['id']
        print(error_message)
        return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=400)

    print("SUCCESS: data with id=%s updated in `SWTable11`." % post_data['id'])
    return HttpResponse(json.dumps({}), content_type='application/json')
