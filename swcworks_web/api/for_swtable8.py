from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic         import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators      import method_decorator
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from datetime import datetime
import json, re

from swcworks_web.models import SWTable8
from swcworks_web import config
from .common_tools import get_user_group, json_load
from .fields_validate import vld_float

@login_required
def getAPIForSWTable8(request, *args, **kwargs):
    ret_data = {'data':[],'total':0}
    print("[%s] ==== Try to get data from `SWTable8`:\nuser: %s" % (timezone.now().strftime('%d/%b/%Y %H:%M:%S'), request.user.username))

    ### Get user's group and make queryset.
    user_group = get_user_group(request)
    if user_group == 'admin':
        queryset = SWTable8.objects.all()
    elif user_group is None:
        error_message = "ERROR: user forbidden."
        print(error_message)
        return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=403)
    else:
        queryset = SWTable8.objects.filter(province = user_group)

    ### make return data.
    ret_data['total'] = queryset.count()
    for obj in queryset.order_by('-id'):
        if obj.t8_type in (1,2,3):
            tmp_data = {'id'         : obj.id,
                        'province'   : config.PROVINCE_DEFINE[obj.province],
                        'type'       : str(obj.t8_type),
                        'touruNum'   : str(obj.zjtrzl),
                        'increase'   : str(obj.jsnzzl),
                        'comments'   : obj.comments,
                        'description': '',
                        }
        else:
            tmp_data = {'id'         : obj.id,
                        'province'   : config.PROVINCE_DEFINE[obj.province],
                        'type'       : str(obj.t8_type),
                        'touruNum'   : '',
                        'increase'   : '',
                        'comments'   : obj.comments,
                        'description': obj.description,
                        }
        ret_data['data'].append(tmp_data)

    print('SUCCESS: %d entries of data returned.' % ret_data['total'])
    return HttpResponse(json.dumps(ret_data), content_type='application/json')


@login_required
@csrf_exempt
def addAPIForSWTable8(request, *args, **kwargs):
    ret_data = {}
    print("[%s] ==== Try to add data to `SWTable8`:\nuser: %s" % (timezone.now().strftime('%d/%b/%Y %H:%M:%S'), request.user.username))

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
        attrs['t8_type'] = int(post_data['type'])
        if attrs['t8_type'] in (1,2,3):
            attrs['zjtrzl'] = vld_float(post_data.get('touruNum'))
            if attrs['zjtrzl'] is None:
                error_message = "ERROR: To add data failed. Field 'touruNum' must be provided and should be a number."
                print(error_message)
                return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=400)

            attrs['jsnzzl'] = vld_float(post_data.get('increase'))
            if attrs['jsnzzl'] is None:
                error_message = "ERROR: To add data failed. Field 'increase' must be provided and should be a number."
                print(error_message)
                return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=400)

            if attrs['t8_type'] == 3 and 'comments' in post_data:
                attrs['comments'] = post_data['comments']

        elif attrs['t8_type'] == 4:
            if not post_data.get('description'):
                attrs['description'] = ''
            else:
                attrs['description'] = post_data['description']
        else:
            error_message = "ERROR: To add data failed. Unsupported value '%s' for field 'type'." % post_data['type']
            print(error_message)
            return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=400)


    attrs['province'] = user_group
    attrs['reporter'] = request.user.username
    attrs['report_time'] = timezone.now()

    ### write data to db.
    obj = SWTable8(**attrs)
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
def deleteAPIForSWTable8(request, *args, **kwargs):
    print("[%s] ==== Try to delete data from `SWTable8`:\nuser: %s" % (timezone.now().strftime('%d/%b/%Y %H:%M:%S'), request.user.username))

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
    queryset = SWTable8.objects.filter(id=post_data['id'])
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

    print("SUCCESS: data with id=%s deleted from `SWTable8`." % post_data['id'])
    return HttpResponse(json.dumps({}), content_type='application/json')


@login_required
@csrf_exempt
def updateAPIForSWTable8(request, *args, **kwargs):
    print("[%s] ==== Try to update data in `SWTable8`:\nuser: %s" % (timezone.now().strftime('%d/%b/%Y %H:%M:%S'), request.user.username))

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
    queryset = SWTable8.objects.filter(id=post_data['id'])
    if queryset.exists():
        obj = queryset.get(id=post_data['id'])
    else:
        error_message = "ERROR: To update data failed, data with id=%s not exist." % post_data['id']
        print(error_message)
        return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=400)

    ### update obj.
    if post_data.get('type'):
        if re.search('^[0-9]+$',str(post_data['type'])) and int(post_data['type']) in SWTable8.TYPE_DEFINE:
            obj.t8_type = int(post_data['type'])
        else:
            error_message = "ERROR: 'level' field must be a number in %s." % str(list(SWTable8.TYPE_DEFINE.keys()))
            print(error_message)
            return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=400)
        if obj.t8_type in (1,2,3):
            if post_data.get('touruNum') is not None:
                # if re.search('^[0-9]+$',str(post_data['touruNum'])):
                #     obj.zjtrzl = int(post_data['touruNum'])
                # else:
                #     error_message = "ERROR: 'touruNum' field must be a number."
                #     print(error_message)
                #     return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=400)
                val = vld_float(post_data['touruNum'])
                if val is None:
                    error_message = "ERROR: 'touruNum' field must be a number."
                    print(error_message)
                    return HttpResponse(json.dumps({'message': error_message}), content_type='application/json', status=400)
                obj.zjtrzl = val

            if post_data.get('increase') is not None:
                val = vld_float(post_data['increase'])
                if val is None:
                    error_message = "ERROR: 'increase' field must be a number."
                    print(error_message)
                    return HttpResponse(json.dumps({'message': error_message}), content_type='application/json', status=400)
                obj.jsnzzl = val
                # if re.search('^[0-9]+$',str(post_data['increase'])):
                #     obj.jsnzzl = int(post_data['increase'])
                # else:
                #     error_message = "ERROR: 'increase' field must be a number."
                #     print(error_message)
                #     return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=400)
            if obj.t8_type == 3 and 'comments' in post_data:
                obj.comments = post_data['comments']
        elif obj.t8_type == 4 and 'description' in post_data:
            obj.description = post_data['description']

    try:
        obj.save()
    except:
        error_message = "ERROR: To update data failed, DB error occured." % post_data['id']
        print(error_message)
        return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=400)

    print("SUCCESS: data with id=%s updated in `SWTable8`." % post_data['id'])
    return HttpResponse(json.dumps({}), content_type='application/json')
