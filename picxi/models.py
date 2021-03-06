from django.db import models
from picxi.util import GUIDModel
# Create your models here.

class InPic(GUIDModel):
    before = models.ImageField(upload_to='dataset/inpic/%Y/%m/%d/', blank=False)
    created = models.DateTimeField(auto_now_add=True)

class SegPic(GUIDModel):
    origin_id = models.ForeignKey(InPic, on_delete=models.CASCADE)
    ing = models.ImageField(upload_to='dataset/segpic/%Y/%m/%d/', blank=False)
    created = models.DateTimeField(auto_now_add=True)

class OutPic(GUIDModel):
    origin_id = models.ForeignKey(SegPic, on_delete=models.CASCADE)
    after = models.ImageField(upload_to='dataset/outpic/%Y/%m/%d/', blank=False)
    created = models.DateTimeField(auto_now_add=True)
