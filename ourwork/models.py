from django.db import models

# Create your models here.
class Ourwork(models.Model):
    company_name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='work')
    date = models.DateTimeField(null=True)

    class Meta:
        verbose_name_plural = "Ourworks"
        ordering=["date"]

    def __str__(self):
        return self.company_name
