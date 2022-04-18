from tabnanny import verbose
from django.db import models
from django.utils import timezone

class BlogModel(models.Model):
    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Bloglar'
    baslik = models.CharField(max_length=200,verbose_name="Başlık")
    icerik = models.TextField(verbose_name="İçerik")
    kayitzamani = models.DateTimeField(default=timezone.now,verbose_name="Kayıt Zamanı")
    yayimzamani = models.DateTimeField(blank=True,null=True,verbose_name="Yayım Zamanı")

    def yayinla(self):
        self.yayimzamani = timezone.now()
        self.save()

    def __str__(self):
        return self.baslik  # TODO burayla ilgili açıklama yapılacak
