# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Qipaoshui(models.Model):
    crawl_time = models.CharField(max_length=255, blank=True, null=True)
    update_time = models.CharField(max_length=255, blank=True, null=True)
    spider_name = models.CharField(max_length=255, blank=True, null=True)
    good_id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'qipaoshui'


class QipaoshuiComment(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    crawl_time = models.CharField(max_length=255, blank=True, null=True)
    update_time = models.CharField(max_length=255, blank=True, null=True)
    good_id = models.CharField(max_length=255, blank=True, null=True)
    pub_time = models.CharField(max_length=255, blank=True, null=True)
    comment_type = models.CharField(max_length=255, blank=True, null=True)
    comment_info = models.CharField(max_length=255, blank=True, null=True)
    spider_name = models.CharField(max_length=255, blank=True, null=True)
    sentiments = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'qipaoshui_comment'


class QipaoshuiSentiments(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    good_id = models.CharField(max_length=255, blank=True, null=True)
    score = models.CharField(max_length=255, blank=True, null=True)
    sentiments = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'qipaoshui_sentiments'
