from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Application(models.Model):
    name = models.CharField(max_length=255)
    number = models.CharField(max_length=255)
    email = models.EmailField()
    cause = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return f"Заявка от {self.name}"
    
    class Meta :
        verbose_name = ""
        verbose_name_plural = "Заявки"

class Index(models.Model):
    title = RichTextField(
        verbose_name='заголовок'
    )
    description = RichTextField(
        verbose_name='описание'
    )
    logo = models.ImageField(
        upload_to='image/',
        verbose_name='Логотип'
    )
    title_2 = models.CharField(
        max_length=255,
        verbose_name='Заголовок (второй)'
    )
    title_3 = models.CharField(
        max_length=255,
        verbose_name='Заголовок (второй 2)'
    )
    description_2 = models.CharField(
        max_length=255,
        verbose_name='Описание (второй)'
    )
    image = models.ImageField(
        upload_to='image/',
        verbose_name='фото'
    )
    title_trips = RichTextField(
        verbose_name='Заголовка ТРИПС'
    ) 
    descriptions_trips = RichTextField(
        verbose_name='описание трипс'
    )

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Настройки главной страницы'

class Icon(models.Model):
    title = models.CharField(
        max_length=15,
        verbose_name='Заголовок иконки'
    )
    icon = models.ImageField(
        upload_to='image/',
        verbose_name='фото иконки'
    )
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Настройки иконки'

class Foto(models.Model):
    title = models.CharField(
        max_length=15,
        verbose_name='Заголовок фотки'
    )
    foto = models.ImageField(
        upload_to='image/',
        verbose_name='фото фотки'
    )
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Настройки фоток'

class Icon2(models.Model):
    title = models.CharField(
        max_length=15,
        verbose_name='Заголовок иконки'
    )
    number = models.CharField(
        max_length=15,
        verbose_name='число иконки'
    )
    foto = models.ImageField(
        upload_to='image/',
        verbose_name='фото иконки'
    )
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Настройки фоток иконки'


class Trips(models.Model):
    data = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создание'
    )
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    price = models.CharField(
        max_length=50,
        verbose_name='Цена'
    )
    image = models.ImageField(
        upload_to='trips/',
        verbose_name='Фото'
    )

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Трипс'

class Blog(models.Model):
    data = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создание'
    )
    image = models.ImageField(
        upload_to='image/',
        verbose_name='фото блога'
    )
    title = models.CharField(
        max_length=20,
        verbose_name='заголовок блога'
    )
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'блог'

class Workers(models.Model):
    image = models.ImageField(
        upload_to='image/',
        verbose_name='фото'
    )
    title = models.CharField(
        max_length=20,
        verbose_name='работа'
    )
    full_name = models.CharField(
        max_length=20,
        verbose_name='имя'
    )
    descriptions = models.TextField(
        verbose_name='описание'
    )
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'рабы'

class MnogoFoto(models.Model):
    title = models.ImageField(
        upload_to='image/',
        verbose_name='фото'
    )
    image2 = models.ImageField(
        upload_to='image/',
        verbose_name='фото2'
    )
    
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'мини фотки'