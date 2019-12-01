from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic         import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators      import method_decorator
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from datetime import datetime
import json, re

from swcworks_web.models import SWTable17
from swcworks_web import config
from .common_tools import get_user_group, json_load

@login_required
def getAPIForSWTable17(request, *args, **kwargs):
    ret_data = {'data':[],'total':0}
    print("[%s] ==== Try to get data from `SWTable17`:\nuser: %s" % (timezone.now().strftime('%d/%b/%Y %H:%M:%S'), request.user.username))

    ### Get user's group and make queryset.
    user_group = get_user_group(request)
    if user_group == 'admin':
        queryset = SWTable17.objects.all()
    elif user_group is None:
        error_message = "ERROR: user forbidden."
        print(error_message)
        return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=403)
    else:
        queryset = SWTable17.objects.filter(province = user_group)

    ### make return data.
    ret_data['total'] = queryset.count()
    for obj in queryset.order_by('-id'):
        tmp_data = {'id'         : obj.id,
                    'province'   : config.PROVINCE_DEFINE[obj.province],
                    'level'      : str(obj.level),
                    'czzj'       : str(obj.czxzj),
                    'cpgyj'      : str(obj.cpgyj),
                    'qtzj'       : str(obj.qtzj),
                    'totalZj'    : str(obj.zjtr_total),
                    'yyglzj'     : str(obj.zfgm),
                    'comment'    : obj.qtzj_comments,
                    }
        ret_data['data'].append(tmp_data)

    print('SUCCESS: %d entries of data returned.' % ret_data['total'])
    return HttpResponse(json.dumps(ret_data), content_type='application/json')


@login_required
@csrf_exempt
def addAPIForSWTable17(request, *args, **kwargs):
    ret_data = {}
    print("[%s] ==== Try to add data to `SWTable17`:\nuser: %s" % (timezone.now().strftime('%d/%b/%Y %H:%M:%S'), request.user.username))

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
    if not post_data.get('comment'):
        error_message = "ERROR: To add data failed. Field 'comment' must be provided."
        print(error_message)
        return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=400)
    else:
        attrs['qtzj_comments'] = post_data['comment']

    if not post_data.get('level') or not re.search('^[0-9]+$',str(post_data['level'])):
        error_message = "ERROR: To add data failed. Field 'level' must be provided and should be a number."
        print(error_message)
        return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=400)
    else:
        attrs['level'] = int(post_data['level'])

    if not post_data.get('czzj') or not re.search('^[0-9]+$',str(post_data['czzj'])):
        error_message = "ERROR: To add data failed. Field 'czzj' must be provided and should be a number."
        print(error_message)
        return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=400)
    else:
        attrs['czxzj'] = int(post_data['czzj'])

    if not post_data.get('cpgyj') or not re.search('^[0-9]+$',str(post_data['cpgyj'])):
        error_message = "ERROR: To add data failed. Field 'cpgyj' must be provided and should be a number."
        print(error_message)
        return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=400)
    else:
        attrs['cpgyj'] = int(post_data['cpgyj'])

    if not post_data.get('qtzj') or not re.search('^[0-9]+$',str(post_data['qtzj'])):
        error_message = "ERROR: To add data failed. Field 'qtzj' must be provided and should be a number."
        print(error_message)
        return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=400)
    else:
        attrs['qtzj'] = int(post_data['qtzj'])

    if not post_data.get('totalZj') or not re.search('^[0-9]+$',str(post_data['totalZj'])):
        error_message = "ERROR: To add data failed. Field 'totalZj' must be provided and should be a number."
        print(error_message)
        return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=400)
    else:
        attrs['zjtr_total'] = int(post_data['totalZj'])

    if not post_data.get('yyglzj') or not re.search('^[0-9]+$',str(post_data['yyglzj'])):
        error_message = "ERROR: To add data failed. Field 'yyglzj' must be provided and should be a number."
        print(error_message)
        return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=400)
    else:
        attrs['zfgm'] = int(post_data['yyglzj'])


    attrs['province'] = user_group
    attrs['reporter'] = request.user.username
    attrs['report_time'] = timezone.now()

    ### write data to db.
    obj = SWTable17(**attrs)
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
def deleteAPIForSWTable17(request, *args, **kwargs):
    print("[%s] ==== Try to delete data from `SWTable17`:\nuser: %s" % (timezone.now().strftime('%d/%b/%Y %H:%M:%S'), request.user.username))

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
    queryset = SWTable17.objects.filter(id=post_data['id'])
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

    print("SUCCESS: data with id=%s deleted from `SWTable17`." % post_data['id'])
    return HttpResponse(json.dumps({}), content_type='application/json')


@login_required
@csrf_exempt
def updateAPIForSWTable17(request, *args, **kwargs):
    print("[%s] ==== Try to update data in `SWTable17`:\nuser: %s" % (timezone.now().strftime('%d/%b/%Y %H:%M:%S'), request.user.username))

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
    queryset = SWTable17.objects.filter(id=post_data['id'])
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
    if post_data.get('czzj'):
        if re.search('^[0-9]+$',str(post_data['czzj'])):
            obj.czzj = int(post_data['czzj'])
        else:
            error_message = "ERROR: 'czzj' field must be a number."
            print(error_message)
            return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=400)
    if post_data.get('cpgyj'):
        if re.search('^[0-9]+$',str(post_data['cpgyj'])):
            obj.cpgyj = int(post_data['cpgyj'])
        else:
            error_message = "ERROR: 'cpgyj' field must be a number."
            print(error_message)
            return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=400)
    if post_data.get('qtzj'):
        if re.search('^[0-9]+$',str(post_data['qtzj'])):
            obj.qtzj = int(post_data['qtzj'])
        else:
            error_message = "ERROR: 'qtzj' field must be a number."
            print(error_message)
            return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=400)
    if post_data.get('totalZj'):
        if re.search('^[0-9]+$',str(post_data['totalZj'])):
            obj.zjtr_total = int(post_data['totalZj'])
        else:
            error_message = "ERROR: 'totalZj' field must be a number."
            print(error_message)
            return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=400)
    if post_data.get('yyglzj'):
        if re.search('^[0-9]+$',str(post_data['yyglzj'])):
            obj.zfgm = int(post_data['yyglzj'])
        else:
            error_message = "ERROR: 'yyglzj' field must be a number."
            print(error_message)
            return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=400)

    if post_data.get('comment'):
        obj.qtzj_comments = post_data['comment']

    try:
        obj.save()
    except:
        error_message = "ERROR: To update data failed, DB error occured." % post_data['id']
        print(error_message)
        return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=400)

    print("SUCCESS: data with id=%s updated in `SWTable17`." % post_data['id'])
    return HttpResponse(json.dumps({}), content_type='application/json')
