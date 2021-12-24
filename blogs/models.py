from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
    
    title = models.CharField("Заголовок" , max_length=200)
    author = models.ForeignKey(User ,null=True , blank=True, on_delete=models.CASCADE)
    text = models.TextField("Текс")
    image = models.ImageField("Картинка", upload_to="img/" , blank=True)
    create = models.DateTimeField("Создан",auto_now_add=True)
    update = models.DateTimeField("Обновлен", auto_now=True)
    moder = models.BooleanField("Модерация",default=False) 

    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        if not self.id:
            self.create = timezone.now()
        self.create = timezone.now()
        return super().save(*args, **kwargs)
    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])