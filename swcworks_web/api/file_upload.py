from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic         import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators      import method_decorator
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django import forms

from datetime import datetime
import json, re, os

from swcworks_web import config
from .common_tools import get_user_group, json_load


class UploadFileForm(forms.Form):
    menu = forms.CharField(max_length=64)
    file = forms.FileField()

def handle_uploaded_file(f, storage_path):
    with open(storage_path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

@csrf_exempt
@login_required
def fileUploador(request, *args, **kwargs):
    print("[%s] ==== Try to receive file from client.\nuser: %s" % (timezone.now().strftime('%d/%b/%Y %H:%M:%S'), request.user.username) )
    if not os.path.isdir(config.FILE_STORAGE_ROOT):
        print("preparing: make FILE_STORAGE_ROOT: %s" % config.FILE_STORAGE_ROOT)
        try:
            os.makedirs(config.FILE_STORAGE_ROOT)
        except:
            error_message = 'ERROR: Server file-system error.'
            print(error_message)
            return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=403)

    ### Check user group.
    user_group = get_user_group(request)
    if user_group is None or user_group == 'admin':
        error_message = 'ERROR: user forbidden to upload any file.'
        print(error_message)
        return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=403)

    if request.method == 'POST':
        ### To make storage directory for user.
        print('menu: %s' % str(request.POST.get('menu')))
        user_storage = os.path.join(config.FILE_STORAGE_ROOT, user_group, request.user.username, str(request.POST.get('menu')))
        if not os.path.isdir(user_storage):
            print("preparing: make user storage dir: %s" % user_storage)
            try:
                os.makedirs(user_storage)
            except:
                error_message = 'ERROR: Server file-system error occured when to makedirs.'
                print(error_message)
                return HttpResponse(json.dumps({'message':error_message}), content_type='application/json', status=403)

        ### Get file data.
        form = UploadFileForm(request.POST, request.FILES)
        print('filename: %s' % str(request.FILES['file']))
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'], os.path.join(user_storage, str(request.FILES['file'])))
            return HttpResponse('To upload file succeeded.')
        else:
            return HttpResponse('Invalid file uploading post.', status=400)
    else:
        return HttpResponse(json.dumps({'message':'ERROR: GET method not support when try to upload files.'}), status = 400)
