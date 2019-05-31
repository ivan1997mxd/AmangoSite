from django.db import models


class Event(models.Model):
    title = models.CharField(verbose_name='标题', max_length=50, help_text='')
    content = models.TextField(verbose_name='内容')

    class Meta:
        verbose_name = '关于'
        verbose_name_plural = '关于我们'

    def __str__(self):
        return "<Event:%s>" % self.title


