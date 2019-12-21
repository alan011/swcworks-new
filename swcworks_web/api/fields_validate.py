import re, json
from django.http import HttpResponse

def vld_choice(value, choices):
    return value if value in choices else None

def vld_int(value, min=0, max=999999999999):
    if re.search('^[0-9]+$', str(value)):
        val = int(value)
        if min <= val <= max:
            return val
    return None

def vld_float(value, min=0.0, max=999999999999.0):
    if re.search(r'^[0-9]+(\.[0-9]+)*$', str(value)):
        val = float(value)
        if min <= val <= max:
            return val
    return None

def check_attrs(post_data, attrs):
    for field in attrs:
        if attrs[field] is None:
            error_message = "ERROR: To add data failed. Invalid value '{}' for field '{}'.".format(
                post_data.get(field), field)
            print(error_message)
            return HttpResponse(json.dumps({'message': error_message}), content_type='application/json', status=400)

def edit_error(value, field, table):
    error_message = "ERROR: Invalid value '{}' for field '{}' in table {}.".format(value, field, table)
    print(error_message)
    return HttpResponse(json.dumps({'message': error_message}), content_type='application/json', status=400)
