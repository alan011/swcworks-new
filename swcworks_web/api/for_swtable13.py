from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic         import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators      import method_decorator
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from datetime import datetime
import json, re

from swcworks_web.models import SWTable13
from swcworks_web import config
from .common_tools import get_user_group, json_load

@login_required
def getAPIForSWTable13(request, *args, **kwargs):
    ret_data = {'data':[],'total':0}
    print("[%s] ==== Try to get data from `SWTable13`:\nuser: %s" % (timezone.now().strftime('%d/%b/%Y %H:%M:%S'), request.user.username))

    ### Get user's group and make queryset.
    user_group = get_user_group(request)
    if user_group == 'admin':
        queryset = SWTable13.objects.all()
    elif user_group is None:
        error_message = "ERROR: user forbidden."
        print(error_message)
        return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=403)
    else:
        queryset = SWTable13.objects.filter(province = user_group)

    ### make return data.
    ret_data['total'] = queryset.count()
    for obj in queryset.order_by('-id'):
        tmp_data = {'id'         : obj.id,
                    'province'   : config.PROVINCE_DEFINE[obj.province],
                    'jbdw'       : obj.jbdw,
                    'pxbmc'      : obj.pxbmc,
                    'content'    : obj.pxlr,
                    'peixunNum'  : str(obj.pxrs),
                    'totalNum'   : str(obj.totalnum),
                    'jiguanTotalNum'  : str(obj.jiguantotalnum),
                    'fuwuzuzhiToalNum': str(obj.fuwuzuzhitoalnum),
                    'otherTotalNum'   : str(obj.othertotalnum),
                    }
        ret_data['data'].append(tmp_data)

    print('SUCCESS: %d entries of data returned.' % ret_data['total'])
    return HttpResponse(json.dumps(ret_data), content_type='application/json')


@login_required
@csrf_exempt
def addAPIForSWTable13(request, *args, **kwargs):
    ret_data = {}
    print("[%s] ==== Try to add data to `SWTable13`:\nuser: %s" % (timezone.now().strftime('%d/%b/%Y %H:%M:%S'), request.user.username))

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
    if post_data.get('jbdw'):
        attrs['jbdw'] = post_data['jbdw']

    if post_data.get('pxbmc'):
        attrs['pxbmc'] = post_data['pxbmc']

    if post_data.get('content'):
        attrs['pxlr'] = post_data['content']

    if post_data.get('peixunNum'):
        if not re.search('^[0-9]+$',str(post_data['peixunNum'])):
            error_message = "ERROR: To add data failed. Field 'peixunNum' must be a number."
            print(error_message)
            return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=400)
        else:
            attrs['pxrs'] = int(post_data['peixunNum'])
    if post_data.get('totalNum'):
        if not re.search('^[0-9]+$',str(post_data['totalNum'])):
            error_message = "ERROR: To add data failed. Field 'totalNum' must be a number."
            print(error_message)
            return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=400)
        else:
            attrs['totalnum'] = int(post_data['totalNum'])

    if post_data.get('jiguanTotalNum'):
        if not re.search('^[0-9]+$',str(post_data['jiguanTotalNum'])):
            error_message = "ERROR: To add data failed. Field 'jiguanTotalNum' must be a number."
            print(error_message)
            return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=400)
        else:
            attrs['jiguantotalnum'] = int(post_data['jiguanTotalNum'])

    if post_data.get('fuwuzuzhiToalNum'):
        if not re.search('^[0-9]+$',str(post_data['fuwuzuzhiToalNum'])):
            error_message = "ERROR: To add data failed. Field 'fuwuzuzhiToalNum' must be a number."
            print(error_message)
            return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=400)
        else:
            attrs['fuwuzuzhitoalnum'] = int(post_data['fuwuzuzhiToalNum'])

    if post_data.get('otherTotalNum'):
        if not re.search('^[0-9]+$',str(post_data['otherTotalNum'])):
            error_message = "ERROR: To add data failed. Field 'otherTotalNum' must be a number."
            print(error_message)
            return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=400)
        else:
            attrs['othertotalnum'] = int(post_data['otherTotalNum'])

    attrs['province'] = user_group
    attrs['reporter'] = request.user.username
    attrs['report_time'] = timezone.now()

    ### write data to db.
    obj = SWTable13(**attrs)
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
def deleteAPIForSWTable13(request, *args, **kwargs):
    print("[%s] ==== Try to delete data from `SWTable13`:\nuser: %s" % (timezone.now().strftime('%d/%b/%Y %H:%M:%S'), request.user.username))

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
    queryset = SWTable13.objects.filter(id=post_data['id'])
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

    print("SUCCESS: data with id=%s deleted from `SWTable13`." % post_data['id'])
    return HttpResponse(json.dumps({}), content_type='application/json')


@login_required
@csrf_exempt
def updateAPIForSWTable13(request, *args, **kwargs):
    print("[%s] ==== Try to update data in `SWTable13`:\nuser: %s" % (timezone.now().strftime('%d/%b/%Y %H:%M:%S'), request.user.username))

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
    queryset = SWTable13.objects.filter(id=post_data['id'])
    if queryset.exists():
        obj = queryset.get(id=post_data['id'])
    else:
        error_message = "ERROR: To update data failed, data with id=%s not exist." % post_data['id']
        print(error_message)
        return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=400)

    ### update obj.
    if post_data.get('jbdw'):
        obj.jbdw = post_data['jbdw']
    if post_data.get('pxbmc'):
        obj.pxbmc = post_data['pxbmc']
    if post_data.get('content'):
        obj.pxlr = post_data['content']

    if post_data.get('peixunNum'):
        if re.search('^[0-9]+$',str(post_data['peixunNum'])):
            obj.pxrs = int(post_data['peixunNum'])
        else:
            error_message = "ERROR: 'peixunNum' field must be a number."
            print(error_message)
            return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=400)

    if post_data.get('totalNum'):
        if not re.search('^[0-9]+$',str(post_data['totalNum'])):
            error_message = "ERROR: To add data failed. Field 'totalNum' must be a number."
            print(error_message)
            return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=400)
        else:
            obj.totalnum = int(post_data['totalNum'])

    if post_data.get('jiguanTotalNum'):
        if not re.search('^[0-9]+$',str(post_data['jiguanTotalNum'])):
            error_message = "ERROR: To add data failed. Field 'jiguanTotalNum' must be a number."
            print(error_message)
            return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=400)
        else:
            obj.jiguantotalnum = int(post_data['jiguanTotalNum'])

    if post_data.get('fuwuzuzhiToalNum'):
        if not re.search('^[0-9]+$',str(post_data['fuwuzuzhiToalNum'])):
            error_message = "ERROR: To add data failed. Field 'fuwuzuzhiToalNum' must be a number."
            print(error_message)
            return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=400)
        else:
            obj.fuwuzuzhitoalnum = int(post_data['fuwuzuzhiToalNum'])

    if post_data.get('otherTotalNum'):
        if not re.search('^[0-9]+$',str(post_data['otherTotalNum'])):
            error_message = "ERROR: To add data failed. Field 'otherTotalNum' must be a number."
            print(error_message)
            return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=400)
        else:
            obj.othertotalnum = int(post_data['otherTotalNum'])

    try:
        obj.save()
    except:
        error_message = "ERROR: To update data failed, DB error occured." % post_data['id']
        print(error_message)
        return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=400)

    print("SUCCESS: data with id=%s updated in `SWTable13`." % post_data['id'])
    return HttpResponse(json.dumps({}), content_type='application/json')
