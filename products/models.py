from django.db import models


class Product(models.Model):
    name = models.CharField(verbose_name='产品名称', max_length=15)
    function = models.TextField(verbose_name='产品功能')
    customer = models.CharField(verbose_name='目标客户', max_length=15)
    case = models.TextField(verbose_name='产品案例')

    class Meta:
        verbose_name = "产品"
        verbose_name_plural = "产品方案"

    def __str__(self):
        return "<Product:%s>" % self.name
