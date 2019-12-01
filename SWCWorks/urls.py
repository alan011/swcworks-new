"""SWCWorks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from swcworks_web.api import *
from swcworks_web.views import myindex, MyLogin, MyLogout
from swcworks_web.db_init import groups_init

groups_init()

urlpatterns = [
    #url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^login/', MyLogin.as_view(), name='mylogin'),
    url(r'^logout', MyLogout.as_view(), name='mylogout'),
    url(r'^file_upload$', fileUploador,name='fileUploador'),
    url(r'^api/v1/zhengcechuangzhi/get', getAPIForSWTable1, name='getAPIForSWTable1'),
    url(r'^api/v1/zhengcechuangzhi/add', addAPIForSWTable1, name='addAPIForSWTable1'),
    url(r'^api/v1/zhengcechuangzhi/delete', deleteAPIForSWTable1, name='deleteAPIForSWTable1'),
    url(r'^api/v1/zhengcechuangzhi/update', updateAPIForSWTable1, name='updateAPIForSWTable1'),
    url(r'^api/v1/xingzhengjigou/get', getAPIForSWTable2, name='getAPIForSWTable2'),
    url(r'^api/v1/xingzhengjigou/add', addAPIForSWTable2, name='addAPIForSWTable2'),
    url(r'^api/v1/xingzhengjigou/delete', deleteAPIForSWTable2, name='deleteAPIForSWTable2'),
    url(r'^api/v1/xingzhengjigou/update', updateAPIForSWTable2, name='updateAPIForSWTable2'),
    url(r'^api/v1/gangwei/get', getAPIForSWTable3, name='getAPIForSWTable3'),
    url(r'^api/v1/gangwei/add', addAPIForSWTable3, name='addAPIForSWTable3'),
    url(r'^api/v1/gangwei/delete', deleteAPIForSWTable3, name='deleteAPIForSWTable3'),
    url(r'^api/v1/gangwei/update', updateAPIForSWTable3, name='updateAPIForSWTable3'),
    url(r'^api/v1/rencaiziyuan/get', getAPIForSWTable4, name='getAPIForSWTable4'),
    url(r'^api/v1/rencaiziyuan/add', addAPIForSWTable4, name='addAPIForSWTable4'),
    url(r'^api/v1/rencaiziyuan/delete', deleteAPIForSWTable4, name='deleteAPIForSWTable4'),
    url(r'^api/v1/rencaiziyuan/update', updateAPIForSWTable4, name='updateAPIForSWTable4'),
    url(r'^api/v1/rencaipeixun/get', getAPIForSWTable5, name='getAPIForSWTable5'),
    url(r'^api/v1/rencaipeixun/add', addAPIForSWTable5, name='addAPIForSWTable5'),
    url(r'^api/v1/rencaipeixun/delete', deleteAPIForSWTable5, name='deleteAPIForSWTable5'),
    url(r'^api/v1/rencaipeixun/update', updateAPIForSWTable5, name='updateAPIForSWTable5'),
    url(r'^api/v1/hangyexiehui/get', getAPIForSWTable6, name='getAPIForSWTable6'),
    url(r'^api/v1/hangyexiehui/add', addAPIForSWTable6, name='addAPIForSWTable6'),
    url(r'^api/v1/hangyexiehui/delete', deleteAPIForSWTable6, name='deleteAPIForSWTable6'),
    url(r'^api/v1/hangyexiehui/update', updateAPIForSWTable6, name='updateAPIForSWTable6'),
    url(r'^api/v1/minbanjigou/get', getAPIForSWTable7, name='getAPIForSWTable7'),
    url(r'^api/v1/minbanjigou/add', addAPIForSWTable7, name='addAPIForSWTable7'),
    url(r'^api/v1/minbanjigou/delete', deleteAPIForSWTable7, name='deleteAPIForSWTable7'),
    url(r'^api/v1/minbanjigou/update', updateAPIForSWTable7, name='updateAPIForSWTable7'),
    url(r'^api/v1/zijintouru/get', getAPIForSWTable8, name='getAPIForSWTable8'),
    url(r'^api/v1/zijintouru/add', addAPIForSWTable8, name='addAPIForSWTable8'),
    url(r'^api/v1/zijintouru/delete', deleteAPIForSWTable8, name='deleteAPIForSWTable8'),
    url(r'^api/v1/zijintouru/update', updateAPIForSWTable8, name='updateAPIForSWTable8'),
    url(r'^api/v1/shehuishidian/get', getAPIForSWTable9, name='getAPIForSWTable9'),
    url(r'^api/v1/shehuishidian/add', addAPIForSWTable9, name='addAPIForSWTable9'),
    url(r'^api/v1/shehuishidian/delete', deleteAPIForSWTable9, name='deleteAPIForSWTable9'),
    url(r'^api/v1/shehuishidian/update', updateAPIForSWTable9, name='updateAPIForSWTable9'),
    url(r'^api/v1/zyfwzhengce/get', getAPIForSWTable10, name='getAPIForSWTable10'),
    url(r'^api/v1/zyfwzhengce/add', addAPIForSWTable10, name='addAPIForSWTable10'),
    url(r'^api/v1/zyfwzhengce/delete', deleteAPIForSWTable10, name='deleteAPIForSWTable10'),
    url(r'^api/v1/zyfwzhengce/update', updateAPIForSWTable10, name='updateAPIForSWTable10'),
    url(r'^api/v1/zyfwzuzhi/get', getAPIForSWTable11, name='getAPIForSWTable11'),
    url(r'^api/v1/zyfwzuzhi/add', addAPIForSWTable11, name='addAPIForSWTable11'),
    url(r'^api/v1/zyfwzuzhi/delete', deleteAPIForSWTable11, name='deleteAPIForSWTable11'),
    url(r'^api/v1/zyfwzuzhi/update', updateAPIForSWTable11, name='updateAPIForSWTable11'),
    url(r'^api/v1/zyzzhuce/get', getAPIForSWTable12, name='getAPIForSWTable12'),
    url(r'^api/v1/zyzzhuce/add', addAPIForSWTable12, name='addAPIForSWTable12'),
    url(r'^api/v1/zyzzhuce/delete', deleteAPIForSWTable12, name='deleteAPIForSWTable12'),
    url(r'^api/v1/zyzzhuce/update', updateAPIForSWTable12, name='updateAPIForSWTable12'),
    url(r'^api/v1/zyzpeixun/get', getAPIForSWTable13, name='getAPIForSWTable13'),
    url(r'^api/v1/zyzpeixun/add', addAPIForSWTable13, name='addAPIForSWTable13'),
    url(r'^api/v1/zyzpeixun/delete', deleteAPIForSWTable13, name='deleteAPIForSWTable13'),
    url(r'^api/v1/zyzpeixun/update', updateAPIForSWTable13, name='updateAPIForSWTable13'),
    url(r'^api/v1/jilugongzuo/get', getAPIForSWTable14, name='getAPIForSWTable14'),
    url(r'^api/v1/jilugongzuo/add', addAPIForSWTable14, name='addAPIForSWTable14'),
    url(r'^api/v1/jilugongzuo/delete', deleteAPIForSWTable14, name='deleteAPIForSWTable14'),
    url(r'^api/v1/jilugongzuo/update', updateAPIForSWTable14, name='updateAPIForSWTable14'),
    url(r'^api/v1/huodongkaizhan/get', getAPIForSWTable15, name='getAPIForSWTable15'),
    url(r'^api/v1/huodongkaizhan/add', addAPIForSWTable15, name='addAPIForSWTable15'),
    url(r'^api/v1/huodongkaizhan/delete', deleteAPIForSWTable15, name='deleteAPIForSWTable15'),
    url(r'^api/v1/huodongkaizhan/update', updateAPIForSWTable15, name='updateAPIForSWTable15'),
    url(r'^api/v1/jilibaozhang/get', getAPIForSWTable16, name='getAPIForSWTable16'),
    url(r'^api/v1/jilibaozhang/add', addAPIForSWTable16, name='addAPIForSWTable16'),
    url(r'^api/v1/jilibaozhang/delete', deleteAPIForSWTable16, name='deleteAPIForSWTable16'),
    url(r'^api/v1/jilibaozhang/update', updateAPIForSWTable16, name='updateAPIForSWTable16'),
    url(r'^api/v1/zyfwzijin/get', getAPIForSWTable17, name='getAPIForSWTable17'),
    url(r'^api/v1/zyfwzijin/add', addAPIForSWTable17, name='addAPIForSWTable17'),
    url(r'^api/v1/zyfwzijin/delete', deleteAPIForSWTable17, name='deleteAPIForSWTable17'),
    url(r'^api/v1/zyfwzijin/update', updateAPIForSWTable17, name='updateAPIForSWTable17'),
    url(r'^.*$', myindex, name='myindex')
]
