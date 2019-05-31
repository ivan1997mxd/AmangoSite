from django.db import models


class Info(models.Model):
    title = models.CharField(verbose_name='标题', max_length=50)
    content = models.TextField(verbose_name='内容')

    class Meta:
        verbose_name = "首页"
        verbose_name_plural = "首页信息"

    def __str__(self):
        return '<Info:%s>' % self.title
