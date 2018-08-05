from django.db import models
from django.utils import timezone
# Create your models here.



class Post(models.Model):    # models : post가 장고 모델임을 의미
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)   #다른 모델에 대한 링크
    title = models.CharField(max_length=200)    #글자수 제한있는 속성
    text = models.TextField()                   #글자수 제한 x
    created_date = models.DateTimeField(default = timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

