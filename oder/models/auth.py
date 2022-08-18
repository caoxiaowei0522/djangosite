# -*- coding:utf-8 -*-
"""
作者：曹小伟
日期：2022年08月17日
"""
from django.contrib.auth.models import AbstractUser
from django.db import models
class User(AbstractUser):
    USER_TYPE=(
        (0,'开发'),
        (1, '测试'),
        (2, '运维'),
        (3, '项目经理'),
    )
    realname=models.CharField('真实姓名',max_length=32),
    phone=models.CharField('手机号码',max_length=11,unique=True,null=True,blank=True),
    user_type=models.SmallIntegerField('用例模型',choices= USER_TYPE,default=1)