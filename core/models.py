from django.db import models
# Create your models here.
class tags(models.Model):
    Tagname=models.CharField(verbose_name='tagname',max_length=50,blank=False,null=True)
    def __str__(self):
        return(self.Tagname)


class blog(models.Model):
    Username=models.CharField(verbose_name='username',max_length=50,blank=False,null=True)
    BlogTitle=models.CharField(verbose_name='Blogtitle',max_length=50,blank=False,null=True)
    BlogDescription=models.CharField(verbose_name='BlogDesc',max_length=50,blank=False,null=True)
    image=models.ImageField(upload_to='CoreImages')
    date= models.DateField(auto_now_add=True)
    tag = models.ForeignKey('tags', verbose_name='Tag', on_delete=models.CASCADE)
    def __str__(self):
        return self.Username