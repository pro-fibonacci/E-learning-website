from django.db import models

# Create your models here.
import datetime
import os

def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/', filename)



class homeModels(models.Model):
	welcome_img = models.ImageField(null=True, blank=True, upload_to ='images/')
	course_img1 = models.ImageField(null=True, blank=True, upload_to ='images/')
	course_img2 = models.ImageField(null=True, blank=True, upload_to ='images/')
	course_img3 = models.ImageField(null=True, blank=True, upload_to ='images/')
	course_img4 = models.ImageField(null=True, blank=True, upload_to ='images/')
	popular_course_img1 = models.ImageField(null=True, blank=True, upload_to ='images/')
	popular_course_img2 = models.ImageField(null=True, blank=True, upload_to ='images/')
	popular_course_img3 = models.ImageField(null=True, blank=True, upload_to ='images/')
	popular_course_price1 = models.IntegerField()
	popular_course_price2 = models.IntegerField()
	popular_course_price3 = models.IntegerField()
	expert_img1 = models.ImageField(null=True, blank=True, upload_to ='images/')
	expert_img2 = models.ImageField(null=True, blank=True, upload_to ='images/')
	expert_img3 = models.ImageField(null=True, blank=True, upload_to ='images/')
	expert_img4 = models.ImageField(null=True, blank=True, upload_to ='images/')
	expert_name1 = models.CharField(max_length=300)
	expert_name2 = models.CharField(max_length=300)
	expert_name3 = models.CharField(max_length=300)
	expert_name4 = models.CharField(max_length=300)



def __str__(self):
	return self.name 


class contacting(models.Model):
	fname= models.CharField( max_length = 1000)
	lname= models.CharField( max_length = 1000)
	email= models.EmailField( max_length = 1000)
	locality= models.CharField( max_length = 1000, default=False)
	address= models.CharField( max_length = 1000)
	state= models.CharField( max_length = 1000)
	country= models.CharField( max_length = 1000)
	dob=models.DateField()
	gender= models.CharField( max_length = 1000)
	phone= models.IntegerField()
	HQ = models.CharField( max_length = 1000)
	CA= models.CharField( max_length = 1000)
	passport = models.ImageField(null=True, blank=True, upload_to="filepath")


def __str__(self):
	return self.name 
