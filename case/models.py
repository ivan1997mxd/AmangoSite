from django.db import models


class Case(models.Model):
    band = models.CharField(verbose_name='项目名称', max_length=50)
    detail = models.TextField(verbose_name='项目简介')

    class Meta:
        verbose_name = "案例"
        verbose_name_plural = "项目案例"

    def __str__(self):
        return '<Case:%s>' % self.band
