from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic         import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators      import method_decorator
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from datetime import datetime
import json, re

from swcworks_web.models import SWTable3
from swcworks_web import config
from .common_tools import get_user_group, json_load

@login_required
def getAPIForSWTable3(request, *args, **kwargs):
    ret_data = {'data':[],'total':0}
    print("[%s] ==== Try to get data from `SWTable3`:\nuser: %s" % (timezone.now().strftime('%d/%b/%Y %H:%M:%S'), request.user.username))

    ### Get user's group and make queryset.
    user_group = get_user_group(request)
    if user_group == 'admin':
        queryset = SWTable3.objects.all()
    elif user_group is None:
        error_message = "ERROR: user forbidden."
        print(error_message)
        return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=403)
    else:
        queryset = SWTable3.objects.filter(province = user_group)

    ### make return data.
    ret_data['total'] = queryset.count()
    for obj in queryset.order_by('-id'):
        tmp_data = {'id'         : obj.id,
                    'province'   : config.PROVINCE_DEFINE[obj.province],
                    'type'       : str(obj.t3_type),
                    'gangweiNum' : str(obj.gwgs),
                    'fuwuzhanNum': str(obj.fwzsz),
                    'otherNum'   : str(obj.wmq),
                    'nojobNum'   : str(obj.shgzr),
                    'comment'   : obj.comments,
                    }
        ret_data['data'].append(tmp_data)

    print('SUCCESS: %d entries of data returned.' % ret_data['total'])
    return HttpResponse(json.dumps(ret_data), content_type='application/json')


@login_required
@csrf_exempt
def addAPIForSWTable3(request, *args, **kwargs):
    ret_data = {}
    print("[%s] ==== Try to add data to `SWTable3`:\nuser: %s" % (timezone.now().strftime('%d/%b/%Y %H:%M:%S'), request.user.username))

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
        attrs['t3_type'] = int(post_data['type'])

    if not post_data.get('gangweiNum') or not re.search('^[0-9]+$',str(post_data['gangweiNum'])):
        error_message = "ERROR: To add data failed. Field 'gangweiNum' must be provided and should be a number."
        print(error_message)
        return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=400)
    else:
        attrs['gwgs'] = int(post_data['gangweiNum'])

    if not post_data.get('fuwuzhanNum') or not re.search('^[0-9]+$',str(post_data['fuwuzhanNum'])):
        error_message = "ERROR: To add data failed. Field 'fuwuzhanNum' must be provided and should be a number."
        print(error_message)
        return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=400)
    else:
        attrs['fwzsz'] = int(post_data['fuwuzhanNum'])

    if not post_data.get('otherNum') or not re.search('^[0-9]+$',str(post_data['otherNum'])):
        error_message = "ERROR: To add data failed. Field 'otherNum' must be provided and should be a number."
        print(error_message)
        return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=400)
    else:
        attrs['wmq'] = int(post_data['otherNum'])

    if not post_data.get('nojobNum') or not re.search('^[0-9]+$',str(post_data['nojobNum'])):
        error_message = "ERROR: To add data failed. Field 'nojobNum' must be provided and should be a number."
        print(error_message)
        return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=400)
    else:
        attrs['shgzr'] = int(post_data['nojobNum'])

    if not post_data.get('comment'):
        attrs['comments'] = ''
    else:
        attrs['comments'] = post_data['comment']

    attrs['province'] = user_group
    attrs['reporter'] = request.user.username
    attrs['report_time'] = timezone.now()

    ### write data to db.
    obj = SWTable3(**attrs)
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
def deleteAPIForSWTable3(request, *args, **kwargs):
    print("[%s] ==== Try to delete data from `SWTable3`:\nuser: %s" % (timezone.now().strftime('%d/%b/%Y %H:%M:%S'), request.user.username))

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
    queryset = SWTable3.objects.filter(id=post_data['id'])
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

    print("SUCCESS: data with id=%s deleted from `SWTable3`." % post_data['id'])
    return HttpResponse(json.dumps({}), content_type='application/json')


@login_required
@csrf_exempt
def updateAPIForSWTable3(request, *args, **kwargs):
    print("[%s] ==== Try to update data in `SWTable3`:\nuser: %s" % (timezone.now().strftime('%d/%b/%Y %H:%M:%S'), request.user.username))

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
    queryset = SWTable3.objects.filter(id=post_data['id'])
    if queryset.exists():
        obj = queryset.get(id=post_data['id'])
    else:
        error_message = "ERROR: To update data failed, data with id=%s not exist." % post_data['id']
        print(error_message)
        return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=400)

    ### update obj.
    if post_data.get('type'):
        if re.search('^[0-9]+$',str(post_data['type'])):
            obj.t3_type = int(post_data['type'])
        else:
            error_message = "ERROR: 'type' field must be a number."
            print(error_message)
            return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=400)

    if post_data.get('gangweiNum'):
        if re.search('^[0-9]+$',str(post_data['gangweiNum'])):
            obj.gwgs = int(post_data['gangweiNum'])
        else:
            error_message = "ERROR: 'gangweiNum' field must be a number."
            print(error_message)
            return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=400)

    if post_data.get('fuwuzhanNum'):
        if re.search('^[0-9]+$',str(post_data['fuwuzhanNum'])):
            obj.fwzsz = int(post_data['fuwuzhanNum'])
        else:
            error_message = "ERROR: 'fuwuzhanNum' field must be a number."
            print(error_message)
            return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=400)

    if post_data.get('otherNum'):
        if re.search('^[0-9]+$',str(post_data['otherNum'])):
            obj.wmq = int(post_data['otherNum'])
        else:
            error_message = "ERROR: 'otherNum' field must be a number."
            print(error_message)
            return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=400)

    if post_data.get('nojobNum'):
        if re.search('^[0-9]+$',str(post_data['nojobNum'])):
            obj.shgzr = int(post_data['nojobNum'])
        else:
            error_message = "ERROR: 'nojobNum' field must be a number."
            print(error_message)
            return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=400)

    if 'comment' in post_data:
        obj.comments = post_data['comment']

    try:
        obj.save()
    except:
        error_message = "ERROR: To update data failed, DB error occured." % post_data['id']
        print(error_message)
        return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=400)

    print("SUCCESS: data with id=%s updated in `SWTable3`." % post_data['id'])
    return HttpResponse(json.dumps({}), content_type='application/json')
