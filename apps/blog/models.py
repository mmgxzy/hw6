from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок для блога")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to="blog_images/", verbose_name="Фотография")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"