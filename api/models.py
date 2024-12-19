from django.db import models


# Create your models here.
class Test(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_dt = models.DateTimeField(auto_now_add=True)
    updated_dt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Text(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    file = models.CharField(verbose_name="파일 이름", max_length=255)
    content = models.TextField(verbose_name="내용")
    created_dt = models.DateTimeField(auto_now=True)
    updated_dt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file
