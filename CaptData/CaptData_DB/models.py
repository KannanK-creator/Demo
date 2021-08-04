from django.db import models

# Create your models here.

# Defining Capture Data Table

class CaptData_Tbl(models.Model):

	CaptData_ID 	= 	models.CharField(blank=False,max_length=50)
	CaptData_Val 	= 	models.CharField(blank=False,max_length=1000)

