from django.db import models

# Create your models here.
class Ablum(models.Model):
    ablum_name = models.CharField(max_length=200)
    ablum_no = models.CharField(max_length=20)
    ablum_pic = models.URLField()
    ablum_des = models.CharField(max_length=300)

    def __str__(self):
        return self.ablum_name

class  Pic(models.Model):
    ablum_no = models.ForeignKey(Ablum,on_delete=models.CASCADE)
    pic_no = models.CharField(max_length=200)
    pic_url = models.URLField()
    pic_text = models.CharField(max_length=200)

    def __str__(self):
        return self.pic_text