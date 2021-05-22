from django.db import models

from django.template.defaultfilters import slugify

# Create your models here.
from django.urls import reverse


class Service(models.Model):
    img_icon = models.ImageField(upload_to='service',null=True)
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    desc = models.CharField(max_length=200)
    img = models.ImageField(upload_to='service_img')

    class Meta:
        ordering = ("name",)
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super(Service, self).save(*args, **kwargs)

    def get_detail_url(self):
        return reverse("essbeeapp:service",kwargs={'c_slug':self.slug})