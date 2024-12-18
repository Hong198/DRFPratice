from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(verbose_name='제목', max_length=255)
    content = models.TextField(verbose_name='내용')
    created_dt = models.DateTimeField(verbose_name="생성 일자", auto_now_add=True)
    updated_dt = models.DateTimeField(verbose_name="수정 일자", auto_now=True)

    def __str__(self):
        return self.title
