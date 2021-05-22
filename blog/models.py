from django.db import models

# Create your models here.
class Blog(models.Model):
    heading=models.CharField(max_length=200)
    desc=models.TextField(blank=True)
    img=models.ImageField(upload_to='blog')
    author=models.CharField(max_length=100,default=None)
    date=models.DateField()
    list_display = ('heading', 'author', 'date')

    class Meta:
        verbose_name_plural = "Blogs"
        ordering = ('-date',)


    def __str__(self):
        return self.heading