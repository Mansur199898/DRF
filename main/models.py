

from django.db import models

# Create your models here.
class Note(models.Model):
    title = models.CharField('Заголовок', max_length=50)
    content = models.TextField('Контент')


    create_at =models.DateField(auto_now_add=True)
    update_at =models.DateField(auto_now=True)


    def __str__(self):
        return self.title