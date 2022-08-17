from django.db import models
from django.conf import settings
class CommonInfo(models.Model):
    # 创建时间
    creat_time=models.DateTimeField('创建时间',auto_now_add=True,null=True)
    # 更新时间
    update_time = models.DateTimeField('更新时间', auto_now=True)
    #描述
    desc = models.TextField(null=True, blank=True, verbose_name='描述')
    # 创建者
    create_by=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.DO_NOTHING,null=True,verbose_name='创建者',
                                related_name='%(class)s_create_by')
    # 更新者
    update_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, null=True, verbose_name='更新者',
                                  related_name='%(class)s_updated_by')
    def __str__(self):
        if hasattr(self,'name'):
            return self.name
        else:
            return self.desc
    class Meta:
        abstract = True  # 当前类为抽象表，字段会被子模型类继承，但是不会创建数据库表 只有abstract这个字段不会被继承
        ordering = ['id']

