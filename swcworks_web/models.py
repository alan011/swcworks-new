from django.db import models
from swcworks_web.config import PROVINCE_DEFINE
from django.utils import timezone
from jsonfield import JSONField
from collections import OrderedDict

# Create your models here.

YES_or_NO = ((0,'No'),(1,'Yes'))

class SWTable1(models.Model):
    ### Table descriptions.
    SWTABLE_NAME     = "表1：出台社会工作政策情况统计表"

    ### DB fields definitions.
    id             = models.AutoField('序号',primary_key=True)
    doc_name       = models.CharField('文件名称',max_length=256, null=True)
    doc_number     = models.CharField('发文文号',max_length=256, null=True)
    release_unit   = models.CharField('发文单位',max_length=256, null=True)
    release_time   = models.DateTimeField('发文时间',default=timezone.now)
    province       = models.CharField('省/直辖市', choices=PROVINCE_DEFINE.items(),max_length=32, null=True)
    reporter       = models.CharField('数据提交人',max_length=256, null=True)
    report_time    = models.DateTimeField('数据提交时间',default=timezone.now)

class SWTable2(models.Model):
    ### Table descriptions.
    SWTABLE_NAME     = "表2：2019年已停用, 2019年也未启用"

    ### Choices definations.
    TYPE_DEFINE  = OrderedDict({
                    1:"编制管理部门批准设立的社会工作处（科、股）",
                    2:"内部设立相对独立的社会工作处（科、股）",
                    3:"在相关处（科、股）加挂社会工作处（科、股）牌子",
                    4:"成立社会工作事业单位",
                   })
    LEVEL_DEFINE = OrderedDict({
                    1:"省级",
                    2:"地市级",
                    3:"县区级",
                   })

    ### DB fields definations.
    id             = models.AutoField('ID',primary_key=True)
    institution    = models.CharField('地区和机构名称',max_length=512, null=True)
    level          = models.IntegerField('级别', choices=LEVEL_DEFINE.items(), null=True)
    inst_type      = models.IntegerField('类别', choices=TYPE_DEFINE.items(), null=True)
    province       = models.CharField('省（区、市）', choices=PROVINCE_DEFINE.items(),max_length=32, null=True)
    reporter       = models.CharField('数据提交人',max_length=256, null=True)
    report_time    = models.DateTimeField('数据提交时间',default=timezone.now)

class SWTable3(models.Model):
    ### Table descriptions.
    SWTABLE_NAME     = "表3：其他单位社会工作岗位开发设置情况统计表"

    ### Choices definations.
    TYPE_DEFINE = OrderedDict({
                    1:"乡镇、街道和社区",
                    2:"民政事业单位", # 2019年已取消此项，后端此处暂时保留
                    3:"其他系统事业单位",
                    4:"社会组织",
                    5:"其他（请在备注注明）",
                    #6:"总计",
                  })

    ### DB fields definitions.
    id             = models.AutoField('序号',primary_key=True)
    t3_type        = models.IntegerField('类别', choices=TYPE_DEFINE.items(), null=True)
    gwgs           = models.IntegerField('岗位个数（个）', null=True)
    fwzsz          = models.IntegerField('社会工作服务站（室、中心）设置情况（个）', null=True)
    wmq            = models.IntegerField('虽未明确为社会工作岗位，但实际岗位职责包括社会工作的（个）', null=True)
    shgzr          = models.IntegerField('已取得社会工作学历学位、职业资格或培训证书，但未从事社会工作的（人）', null=True)
    comments       = models.TextField('备注说明', null=True)
    province       = models.CharField('省（区、市）', choices=PROVINCE_DEFINE.items(),max_length=32, null=True)
    reporter       = models.CharField('数据提交人',max_length=256, null=True)
    report_time    = models.DateTimeField('数据提交时间',default=timezone.now)

# class SWTable4(models.Model):
#     ### Table descriptions.
#     SWTABLE_NAME     = "表4：社会工作专业人才资源情况统计表"
#     SWTABLE_COMMENTS = "1.社会工作专业人才定义参照《中央组织部办公厅、民政部办公厅关于开展全国社会工作专业人才资源统计的通知》（民办函〔2016〕151号）；\n2.请民政部门积极协调相关部门提供数据，对于无法提供数据的部门不作强行要求；\n3.统计截止日期根据各部门实际掌握的数据情况确定，越新越好，请具体注明。"
#
#     ### Choices definations.
#     TYPE_DEFINE = {
#                     1:"民政",
#                     2:"公安（禁毒办）",
#                     3:"司法行政",
#                     4:"扶贫",
#                     5:"工会",
#                     6:"共青团",
#                     7:"综治",
#                     8:"教育",
#                     9:"人力社保",
#                     10:"卫生计生",
#                     11:"信访",
#                     12:"妇联",
#                     13:"残联",
#                     #14:"总计",
#                   }
#
#     ### DB fields definitions.
#     id             = models.AutoField('ID',primary_key=True)
#     t4_type        = models.IntegerField('类别', choices=TYPE_DEFINE.items(), null=True)
#     rcsl           = models.IntegerField('人才数量（人）', null=True)
#     shjzrq         = models.DateTimeField('数据截止日期',default=timezone.now)
#     # shgzzycc_total = models.IntegerField('社会工作专业人才总量', null=True)
#     province       = models.CharField('数据所属省份', choices=PROVINCE_DEFINE.items(),max_length=32, null=True)
#     reporter       = models.CharField('数据提交人',max_length=256, null=True)
#     report_time    = models.DateTimeField('数据提交时间',default=timezone.now)

class SWTable4(models.Model):
    ### Table descriptions.
    SWTABLE_NAME     = "表4：社会工作专业人才资源情况统计表"

    ### Choices definations.
    TYPE_DEFINE = OrderedDict({
                    1:"民政",
                    2:"公安（禁毒办）",
                    3:"司法行政",
                    4:"扶贫",
                    5:"工会",
                    6:"共青团",
                    7:"综治",
                    8:"教育",
                    9:"人力社保",
                    10:"卫生计生",
                    11:"信访",
                    12:"妇联",
                    13:"残联",
                    #14:"总计",
                  })

    ### DB fields definitions.
    id             = models.AutoField('序号',primary_key=True)
    minzheng       = models.IntegerField('民政', default=0)
    gongan         = models.IntegerField('公安（禁毒办）', default=0)
    sifaxingzheng  = models.IntegerField('司法行政', default=0)
    fupin          = models.IntegerField('扶贫', default=0)
    gonghui        = models.IntegerField('工会', default=0)
    gongqingtuan   = models.IntegerField('共青团', default=0)
    zongzhi        = models.IntegerField('综治', default=0)
    jiaoyu         = models.IntegerField('教育', default=0)
    renlishebao    = models.IntegerField('人力社保', default=0)
    weishengjisheng = models.IntegerField('卫健', default=0)
    xinfang        = models.IntegerField('信访', default=0)
    fulian         = models.IntegerField('妇联', default=0)
    canlian        = models.IntegerField('残联', default=0)
    province       = models.CharField('省（市、区）', choices=PROVINCE_DEFINE.items(),max_length=32, null=True)
    reporter       = models.CharField('数据提交人',max_length=256, null=True)
    report_time    = models.DateTimeField('数据提交时间',default=timezone.now)

class SWTable5(models.Model):
    ### Table descriptions.
    SWTABLE_NAME     = "表5：社会工作专业人才培训情况统计表"

    ### Choices definations.
    YEAR_TAG_DEFINE = OrderedDict({
                        '2019':'2019年社会工作培训情况',
                      })

    ### DB fields definitions.
    id             = models.AutoField('序号',primary_key=True)
    year_tag       = models.CharField('统计年份', max_length=8, choices=YEAR_TAG_DEFINE.items(), null=True)
    pxrc           = models.IntegerField('培训人次', null=True)
    jqnzzl         = models.IntegerField('较去年增长量', null=True)
    zheng_ti_gui_hua = models.TextField('社会工作人才纳入本省（区市）人才培养整体规划情况:',  default="")
    province       = models.CharField('省（市、区）', choices=PROVINCE_DEFINE.items(),max_length=32, null=True)
    reporter       = models.CharField('数据提交人',max_length=256, null=True)
    report_time    = models.DateTimeField('数据提交时间',default=timezone.now)

class SWTable6(models.Model):
    ### Table descriptions.
    SWTABLE_NAME     = "表6：社会工作行业协会情况统计表"

    ### Choices definations.
    LEVEL_DEFINE = OrderedDict({
                    1:'在省级民政部门登记的',
                    2:'在地市级民政部门登记的',
                    3:'在县区级民政部门登记的',
                   })

    ### DB fields definitions.
    id             = models.AutoField('序号',primary_key=True)
    level          = models.IntegerField('级别', choices=LEVEL_DEFINE.items(), null=True)
    shgzhyxhgs     = models.IntegerField('社会工作行业协会数量（个）', null=True)
    cldzzsl        = models.IntegerField('成立党组织数量（个）', null=True)
    xiehuiorgnum   = models.IntegerField('行业协会单位会员数量（个）', null=True)
    xiehuipernum   = models.IntegerField('行业协会个人会员数量（个）', null=True)
    province       = models.CharField('省（市、区）', choices=PROVINCE_DEFINE.items(),max_length=32, null=True)
    reporter       = models.CharField('数据提交人',max_length=256, null=True)
    report_time    = models.DateTimeField('数据提交时间',default=timezone.now)

class SWTable7(models.Model):
    ### Table descriptions.
    SWTABLE_NAME     = "表7：民办社会工作服务机构情况统计表"

    LEVEL_DEFINE = OrderedDict({
                    1:'省级民政部门登记',
                    2:'地市级民政部门登记',
                    3:'县区级民政部门登记',
                   })

    ### DB fields definitions.
    id             = models.AutoField('序号',primary_key=True)
    level          = models.IntegerField('级别', choices=LEVEL_DEFINE.items(), null=True)
    jgsl           = models.IntegerField('机构数量（个）', null=True)
    zzgzrysl       = models.IntegerField('专职工作人员数量（人）', null=True)
    jcdzzsl        = models.IntegerField('机构中经过上级党组织批准设立的基层党组织数量（个）', null=True)
    # cldzzsl        = models.IntegerField('成立党组织数量（个）', null=True)
    dysl           = models.IntegerField('专职工作人员中的党员数量（人）', null=True)
    province       = models.CharField('省（市、区）', choices=PROVINCE_DEFINE.items(),max_length=32, null=True)
    reporter       = models.CharField('数据提交人',max_length=256, null=True)
    report_time    = models.DateTimeField('数据提交时间',default=timezone.now)

# class SWTable7Attach(models.Model):
#     ### Table descriptions.
#     SWTABLE_NAME     = "表7：民办社会工作服务机构情况统计表（子表）"
#     SWTABLE_COMMENTS = ""
#
#     ### Choices definations.
#     LEVEL_DEFINE = {
#                     1:'省级民政部门登记的民办社会工作服务机构数量',
#                     2:'地市级民政部门登记的民办社会工作服务机构数量',
#                     3:'县区级民政部门登记的民办社会工作服务机构数量',
#                    }
#
#     ### DB fields definitions.
#     id             = models.AutoField('ID',primary_key=True)
#     level          = models.IntegerField('级别', choices=LEVEL_DEFINE.items(), null=True)
#     mbshgzfwjgsl   = models.IntegerField('民办社会工作服务机构数量', null=True)
#     province       = models.CharField('数据所属省份', choices=PROVINCE_DEFINE.items(),max_length=32, null=True)
#     reporter       = models.CharField('数据提交人',max_length=256, null=True)
#     report_time    = models.DateTimeField('数据提交时间',default=timezone.now)

class SWTable8(models.Model):
    ### Table descriptions.
    SWTABLE_NAME     = "表8：社会工作资金投入情况统计表"

    ### Choices definations.
    TYPE_DEFINE      = OrderedDict({
                        1:'本省范围财政性资金',
                        2:'本省范围福利彩票公益金',
                        3:'本省范围其他资金',
                        4:'“民政部本级彩票金社会工作和志愿服务项目”资金执行、结余情况及主要服务项目（活动）开展情况',
                     })

    ### DB fields definitions.
    id             = models.AutoField('序号',primary_key=True)
    t8_type        = models.IntegerField('类别', choices=TYPE_DEFINE.items(), null=True)
    zjtrzl         = models.FloatField('2019年资金投入总量（万元）', null=True)
    jsnzzl         = models.FloatField('较上年增长量（万元）', null=True)
    comments       = models.TextField('备注其他资金来源', default='')
    description    = models.TextField('“民政部本级彩票金社会工作和志愿服务项目”资金使用方式及用途（开展项目、活动名称及简介）', default='')
    province       = models.CharField('省（市、区）', choices=PROVINCE_DEFINE.items(),max_length=32, null=True)
    reporter       = models.CharField('数据提交人',max_length=256, null=True)
    report_time    = models.DateTimeField('数据提交时间',default=timezone.now)

class SWTable9(models.Model):
    ### Table descriptions.
    SWTABLE_NAME     = "表9：社会工作试点示范、工程、计划、项目开展情况统计表"

    ### Choices definations.
    TYPE_DEFINE    = OrderedDict({
                        1:'社会工作参与脱贫攻坚示范项目',
                        2:'社会工作试点示范',
                        3:'社会工作工程、计划、项目',
                     })

    ### DB fields definitions.
    id             = models.AutoField('序号',primary_key=True)
    t9_type        = models.IntegerField('类别',choices=TYPE_DEFINE.items(), null=True)
    name           = models.CharField('名称', max_length=256, null=True)
    zyqkjs         = models.TextField('主要情况简介', null=True)
    kzddqhdwmc     = models.TextField('开展的地区和单位名称', null=True)
    num            = models.IntegerField('覆盖贫困地区县/村数量（个）', null=True)
    trzj           = models.FloatField('投入资金（万元）', null=True)
    province       = models.CharField('省（市、区）', choices=PROVINCE_DEFINE.items(),max_length=32, null=True)
    reporter       = models.CharField('数据提交人',max_length=256, null=True)
    report_time    = models.DateTimeField('数据提交时间',default=timezone.now)

class SWTable10(models.Model):
    ### Table descriptions.
    SWTABLE_NAME     = "表10：出台志愿服务政策情况统计表"

    ### DB fields definitions.
    id             = models.AutoField('序号',primary_key=True)
    doc_name       = models.CharField('文件名称',max_length=256, null=True)
    doc_number     = models.CharField('发文文号',max_length=256, null=True)
    release_unit   = models.CharField('发文单位',max_length=256, null=True)
    release_time   = models.DateTimeField('发文时间',default=timezone.now)
    province       = models.CharField('省/直辖市', choices=PROVINCE_DEFINE.items(),max_length=32, null=True)
    reporter       = models.CharField('数据提交人',max_length=256, null=True)
    report_time    = models.DateTimeField('数据提交时间',default=timezone.now)

class SWTable11(models.Model):
    ### Table descriptions.
    SWTABLE_NAME     = "表11：志愿服务组织情况统计表"
    FIELD_HAT      = "在民政部门登记的志愿服务组织数"
    FIELDS_NEED_HAT = ('shtt','shfwjg','jjh')

    ### Choices definations.
    LEVEL_DEFINE   = OrderedDict({
                        1:'省级',
                        2:'地市级',
                        3:'县区级',
                     })

    ### DB fields definitions.
    id             = models.AutoField('序号',primary_key=True)
    level          = models.IntegerField('级别', choices=LEVEL_DEFINE.items(), null=True)
    area_name      = models.CharField('地区名称', max_length=64, null=True)
    shtt           = models.IntegerField('社会团体', null=True)
    shfwjg         = models.IntegerField('社会服务机构', null=True)
    jjh            = models.IntegerField('基金会', null=True)
    zyfwzzs        = models.IntegerField('单位和社区内部成立的志愿服务组织数（个）', null=True)
    sqtotalnum     = models.IntegerField('社区内部成立的志愿服务队伍总数（个）', null=True)
    totalnum       = models.IntegerField('全省社区志愿服务站点数（个）', null=True)
    province       = models.CharField('省（市、区）', choices=PROVINCE_DEFINE.items(),max_length=32, null=True)
    reporter       = models.CharField('数据提交人',max_length=256, null=True)
    report_time    = models.DateTimeField('数据提交时间',default=timezone.now)

class SWTable12(models.Model):
    ### Table descriptions.
    SWTABLE_NAME     = "表12：志愿者注册情况统计表"

    ### DB fields definitions.
    id             = models.AutoField('序号',primary_key=True)
    zczyzzs        = models.IntegerField('注册志愿者总数（人）', null=True)
    bl             = models.FloatField('注册志愿者占当地居民人口总数的比例（%）', null=True)
    qg_zyzs        = models.IntegerField('在全国志愿服务信息系统中的注册志愿者数（人）', null=True)
    province       = models.CharField('省（市、区）', choices=PROVINCE_DEFINE.items(),max_length=32, null=True)
    reporter       = models.CharField('数据提交人',max_length=256, null=True)
    report_time    = models.DateTimeField('数据提交时间',default=timezone.now)

class SWTable13(models.Model):
    ### Table descriptions.
    SWTABLE_NAME     = "表13：志愿者培训情况统计表"

    ### DB fields definitions.
    id             = models.AutoField('序号',primary_key=True)
    jbdw           = models.CharField('举办单位', max_length=256, null=True)
    pxbmc          = models.CharField('培训班名称', max_length=256, null=True)
    pxlr           = models.TextField('培训内容', null=True)
    pxrs           = models.IntegerField('培训人数', null=True)
    totalnum       = models.IntegerField('2019年全省范围内志愿者培训总人数', null=True)
    jiguantotalnum = models.IntegerField('党政机关组织培训的志愿者总人数', null=True)
    fuwuzuzhitoalnum = models.IntegerField('志愿服务组织培训的志愿者总人数', null=True)
    othertotalnum  = models.IntegerField('其他组织培训的志愿者总人数', null=True)
    province       = models.CharField('省（市、区）', choices=PROVINCE_DEFINE.items(),max_length=32, null=True)
    reporter       = models.CharField('数据提交人',max_length=256, null=True)
    report_time    = models.DateTimeField('数据提交时间',default=timezone.now)



class SWTable14(models.Model):
    ### Table descriptions.
    SWTABLE_NAME     = "表15：志愿服务记录工作开展情况统计表"
    FIELD_HAT      = "开展志愿服务记录工作的地方和单位数量（个）"
    FIELDS_NEED_HAT = ('xsl','jsl','sqsl','dwsl')

    ### DB fields definitions.
    id             = models.AutoField('序号',primary_key=True)
    area_name      = models.CharField('出台志愿服务记录实施方案的地区名称', max_length=256, null=True)
    xsl            = models.IntegerField('县（市、区）数量', null=True)
    jsl            = models.IntegerField('街（镇）数量', null=True)
    sqsl           = models.IntegerField('社区数量', null=True)
    dwsl           = models.IntegerField('单位数量', null=True)
    province       = models.CharField('省（市、区）', choices=PROVINCE_DEFINE.items(),max_length=32, null=True)
    reporter       = models.CharField('数据提交人',max_length=256, null=True)
    report_time    = models.DateTimeField('数据提交时间',default=timezone.now)

class SWTable15(models.Model):
    ### Table descriptions.
    SWTABLE_NAME     = "表14：志愿服务活动开展情况统计表"

    ### DB fields definitions.
    id             = models.AutoField('序号',primary_key=True)
    zyfwzss        = models.IntegerField('志愿服务总时数（小时）', null=True)
    nzyfwss        = models.IntegerField('其中：2019年志愿服务时数（小时）', null=True)
    zdzyfwhd       = models.TextField('省级重点志愿服务活动名称及简介', default='')
    province       = models.CharField('省（市、区）', choices=PROVINCE_DEFINE.items(),max_length=32, null=True)
    reporter       = models.CharField('数据提交人',max_length=256, null=True)
    report_time    = models.DateTimeField('数据提交时间',default=timezone.now)

class SWTable16(models.Model):
    ### Table descriptions.
    SWTABLE_NAME     = "表16：志愿者激励保障情况统计表"
    FIELD_HAT        = "全省用于激励保障的资金投入量（万元）"
    FIELDS_NEED_HAT  = ('zyzccs','czzjtr')

    ### DB fields definitions.
    id             = models.AutoField('序号',primary_key=True)
    zyzccs         = models.TextField('本地区激励保障志愿者的主要政策措施', null=True)
    czzjtr         = models.FloatField('2019年财政资金投入', null=True)
    fcjtr          = models.FloatField('2019年福彩金投入', null=True)
    province       = models.CharField('省（市、区）', choices=PROVINCE_DEFINE.items(),max_length=32, null=True)
    reporter       = models.CharField('数据提交人',max_length=256, null=True)
    report_time    = models.DateTimeField('数据提交时间',default=timezone.now)

class SWTable17(models.Model):
    ### Table descriptions.
    SWTABLE_NAME     = "表17：志愿服务资金投入情况统计表"

    ### Choices definations.
    LEVEL_DEFINE = OrderedDict({
                    1:"省级层面",
                    2:"全省总计投入资金",
                   })

    ### DB fields definitions.
    id             = models.AutoField('序号',primary_key=True)
    level          = models.IntegerField('级别', choices=LEVEL_DEFINE.items(), null=True)
    czxzj          = models.FloatField('2019年财政性资金（万元）', null=True)
    cpgyj          = models.FloatField('2019年彩票公益金（万元）', null=True)
    qtzj           = models.FloatField('2019年其他资金（万元）', null=True)
    qtzj_comments  = models.TextField('其他资金备注', null=True)
    zjtr_total     = models.FloatField('2019年总计投入', null=True)
    zfgm           = models.FloatField('其中：政府购买志愿服务运营管理的资金（万元）', null=True)
    province       = models.CharField('省（市、区）', choices=PROVINCE_DEFINE.items(),max_length=32, null=True)
    reporter       = models.CharField('数据提交人',max_length=256, null=True)
    report_time    = models.DateTimeField('数据提交时间',default=timezone.now)


class SWTable2For2019(models.Model):
    # 2019年新增的表。取代2017年以前的表2
    SWTABLE_NAME = "表2：民政事业单位社会工作岗位开发设置情况统计表"
    TYPE_CHOICES = ["养老机构","精神疾病服务机构", "儿童福利机构", "救助管理机构", "殡葬服务机构", "婚姻家庭服务机构", "其他（请注明）"]

    id = models.AutoField('序号', primary_key=True)
    jigou_type = models.CharField("机构类别", max_length=128, default="")  # choice from TYPE_CHOICES
    qitajigou_comment = models.TextField("其他机构备注", default="")
    zongshu = models.IntegerField("机构总数量（个）", default=0)
    szsgks = models.IntegerField("设置社工科（室）的机构数量（个）", default=0)
    wszsgks = models.IntegerField("未设置社工科（室）但设有社工岗位的机构数量（个）", default=0)
    sggw = models.IntegerField("社工岗位数量（个）", default=0)
    province = models.CharField('省（市、区）', choices=PROVINCE_DEFINE.items(), max_length=32, null=True)
    reporter = models.CharField('数据提交人', max_length=256, null=True)
    report_time = models.DateTimeField('数据提交时间', default=timezone.now)

    fields = ['id', 'jigou_type', 'qitajigou_comment', 'zongshu', 'szsgks', 'wszsgks', 'sggw', 'province']

