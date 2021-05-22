
from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
from django.urls import reverse


class LatestNews(models.Model):
    img=models.ImageField(upload_to='news')
    heading=models.CharField(max_length=255,unique=True)
    slug=models.SlugField(max_length=255,unique=True)
    sub_heading=models.CharField(max_length=255)
    desc=models.TextField()

    class Meta:
        ordering = ("heading",)
        verbose_name = 'LatestNews'
        verbose_name_plural = 'LatestNews'

    def __str__(self):
        return self.heading

    def save(self, *args, **kwargs):
        self.slug = slugify(self.heading)
        return super(LatestNews, self).save(*args, **kwargs)

    def get_url(self):
        return reverse("essbeeapp:latestNews",kwargs={'n_slug':self.slug})
