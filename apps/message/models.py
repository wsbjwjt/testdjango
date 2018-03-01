# -*- encoding: UTF-8 -*-

from django.db import models

# Create your models here.

# 继承于django.db.models.Model
class UserMessage(models.Model):

    object_id = models.CharField(primary_key=True, max_length=50, default="", verbose_name=u"主键")
    name = models.CharField(max_length=20, null=True, blank=True, verbose_name=u"用户名")

    email = models.EmailField(verbose_name=u"邮箱")

    address = models.CharField(max_length=100, verbose_name=u"地址")

    message = models.CharField(max_length=500, verbose_name=u"留言板")

    class Meta:
        verbose_name = u"用户留言信息"
        # db_table ，这里我们让它自动生成所以不用指定

        # db_table = "user_message"
        # ordering = "-object_id"

        verbose_name_plural = verbose_name