from django.db import models

# Create your models here.
class Parameters(models.Model):
	title= models.CharField(max_length=50,verbose_name='First Name',null=True)
	title3= models.CharField(max_length=50,verbose_name='Last Name',null=True)
	phone= models.IntegerField(verbose_name='Phone No.',null=True)
	email= models.EmailField(max_length=50,verbose_name='Email Id',null=True)

	def __str__(self):
		return self.name

