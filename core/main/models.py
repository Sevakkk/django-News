from django.db import models

# Create your models here.
class Phone(models.Model):
    name = models.CharField('Phone name', max_length=20)
    price = models.IntegerField('Phone price')
    img = models.ImageField('Phone image', upload_to='media')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Phone'
        verbose_name_plural = 'Phones'

class News(models.Model):
    name = models.CharField('News name', max_length=50)
    about = models.TextField('News about')
    img = models.ImageField('News image', upload_to='media')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'