from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True)
    #연,월,일로 내려가면서 저장하여 유저를 분산시켜야 서버 속도에 유리하다.
    #blank의 의미는 빈칸이어도 상관 없다는 뜻이다.
    

    def __str__(self):
        return f'[{self.pk}]{self.title}'
        #pk는 고유 레코드값, 

    def get_absolute_url(self):
        return f'/blog/{self.pk}/'