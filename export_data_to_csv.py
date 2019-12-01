#!/usr/local/python3

import os, sys, json, django, csv
from collections import OrderedDict

sys.path.append('/var/django_projects/SWCWorks')
#os.environ['DJANGO_SETTING_MODULE']='geniusalt_project.settings'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SWCWorks.settings")
django.setup()

from django.contrib.auth.models import Group, User
from swcworks_web.config import PROVINCE_DEFINE
from swcworks_web.models import *

out_dir='/root/swc_data_export'


translate_fields = OrderedDict({
    SWTable1:{},
    SWTable2:{},
    SWTable3:{'t3_type':SWTable3.TYPE_DEFINE},
    SWTable4:{},
    SWTable5:{},
    SWTable6:{'level':SWTable6.LEVEL_DEFINE},
    SWTable7:{'level':SWTable7.LEVEL_DEFINE},
    SWTable8:{'t8_type':SWTable8.TYPE_DEFINE},
    SWTable9:{'t9_type':SWTable9.TYPE_DEFINE},
    SWTable10:{},
    SWTable11:{'level':SWTable11.LEVEL_DEFINE},
    SWTable12:{},
    SWTable13:{},
    SWTable14:{},
    SWTable15:{},
    SWTable16:{},
    SWTable17:{'level':SWTable17.LEVEL_DEFINE},
})


def prepare():
    if not os.path.isdir(out_dir):
        os.makedirs(out_dir)

def export_one_table(model):
    file_name=model.SWTABLE_NAME + '.csv'
    file_path=os.path.join(out_dir, file_name)
    queryset = model.objects.all()
    fields = model._meta.get_fields()
    field_names = [fld.name for fld in fields]
    header = [fld.verbose_name for fld in fields]
    data = []
    for obj in queryset:
        one_line = []
        for fld in field_names:
            fld_data = getattr(obj, fld)
            if fld in translate_fields[model]:
                fld_data = translate_fields[model][fld][fld_data]
            if fld == 'province':
                fld_data = PROVINCE_DEFINE[fld_data]
            one_line.append(fld_data)

        data.append(tuple(one_line))

    with open(file_path, 'w') as f:
        f_csv = csv.writer(f)
        f_csv.writerow(header)
        f_csv.writerows(data)


#------------------- main --------------
if __name__ == '__main__':
    prepare()

    for model in translate_fields.keys():
        print(model.SWTABLE_NAME)
        export_one_table(model)
