from django.db import models


class Contact(models.Model):
    position = models.CharField(verbose_name='地点', max_length=50)
    address = models.CharField(verbose_name='地址', max_length=50)
    telephone = models.CharField(verbose_name='电话', max_length=50)
    email = models.CharField(verbose_name='电子邮箱', max_length=50)

    class Meta:
        verbose_name = '联系'
        verbose_name_plural = '联系方式'

    def __str__(self):
        return "<Contact:%s>" % self.position
