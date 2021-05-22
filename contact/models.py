from django.db import models

# Create your models here.


class Contact(models.Model):
    name=models.CharField(max_length=100,blank=False,null=False)
    from_email = models.EmailField()
    mobile_num=models.IntegerField(default=None)
    message = models.TextField()
    date=models.DateTimeField(auto_now=True)


    class Meta:
      verbose_name_plural = "Contacts"



    def __str__(self):
       return self.name + "-" + self.from_email
