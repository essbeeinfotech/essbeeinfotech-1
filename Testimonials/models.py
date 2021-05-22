from django.db import models

# Create your models here.
class Testimonials(models.Model):
    author=models.CharField(max_length=100,default=None)
    job_position=models.CharField(max_length=100,default=None)
    img=models.ImageField(upload_to='testimonials',default=None)
    desc=models.TextField(blank=True)
    class Meta:
        verbose_name_plural = "Testimonials"

    def __str__(self):
        return self.author

    list_display=('author','job_position')