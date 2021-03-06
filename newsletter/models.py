from django.db import models

# Create your models here.
class SignUp(models.Model):
	email = models.EmailField(blank=False)
	full_name = models.CharField(max_length=30,blank=True,null=True)
	timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
	updated=models.DateTimeField(auto_now_add=False,auto_now=True)

	def __unicode__(self):
		return self.email

# Create your models here.
class BlogPost(models.Model):
	blogtitle = models.CharField(max_length=30,blank=True,null=True)
	content = models.TextField(blank=True,null=True)
	timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)

	def __unicode__(self):
		return self.blogtitle or u''
